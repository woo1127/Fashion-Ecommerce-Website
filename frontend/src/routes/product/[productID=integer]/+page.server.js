/** @type {import('./$types').PageServerLoad} */
export async function load({ params, locals }) {
    const res = await fetch(`http://127.0.0.1:5000/api/product/${params.productID}`)
    const json = await res.json();

    if (!res.ok) 
        error(json.code || 400, { message: json.message })

    return { 
        product: json.data, 
        access_token: locals.accessToken, 
        user_id:  locals.userID 
    }
}