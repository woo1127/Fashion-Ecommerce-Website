/** @type {import('./$types').PageServerLoad} */
export async function load({ locals }) {
    const headers = { 'Authorization': `Bearer ${locals.accessToken}` }
    const res = await fetch('http://127.0.0.1:5000/api/cart/get_cart_count', { method: 'GET', headers })
    const json = await res.json()
    
    return {
        user: locals.accessToken || null,
        cart_item_count: json.data || 0
    }
}