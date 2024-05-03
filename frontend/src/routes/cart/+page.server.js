import { error } from '@sveltejs/kit'

/** @type {import('./$types').PageServerLoad} */
export async function load({ locals }) {
    const res = await fetch('http://127.0.0.1:5000/api/cart/get_cart_info', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + locals.accessToken
        }
    })
    const json = await res.json()

    if (!res.ok) error(400, json.message)

    return { carts: json.data, access_token: locals.accessToken }
}