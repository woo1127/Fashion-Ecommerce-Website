import { error, fail } from '@sveltejs/kit'


/** @type {import('./$types').PageServerLoad} */
export async function load({ locals }) {
    const headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + locals.accessToken
    }

    const cartRes = await fetch('http://127.0.0.1:5000/api/cart/get_cart_info', { method: 'POST', headers })
    const cartJson = await cartRes.json()

    const userRes = await fetch('http://127.0.0.1:5000/api/auth/get_user_info', { method: 'GET', headers })
    const userJson = await userRes.json()

    if (!cartRes.ok) error(cartJson.code || 400, cartJson.message)
    if (!userRes.ok) error(userJson.code || 400, userJson.message)

    return {
        carts: cartJson.data, 
        user: userJson.data,
        access_token: locals.accessToken
    }
}


/** @type {import('./$types').Actions} */
export const actions = {
    address: async({ request, cookies }) => {
        const formData = await request.formData()
        const username = formData.get('name')
        const phone_number = formData.get('phone')
        const address = formData.get('address')

        if (!username || !phone_number || !address) 
            fail(400, { message: 'Please fill in all the required fields', error: true })

        const res = await fetch(`http://127.0.0.1:5000/api/auth/update/${cookies.get('user_id')}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + cookies.get('access_token') },
            body: JSON.stringify({ 
                update_fields: {
                    username: username,
                    phone_number: phone_number,
                    address: address
                }
            })
        })
        const json = await res.json()

        if (!res.ok) 
            fail(json.code || 400, { message: json.message, error: true })

        return {
            user: json.data
        }
    }
}