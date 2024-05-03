import { error } from '@sveltejs/kit'

/** @type {import('./$types').PageServerLoad} */
export async function load({ locals, params }) {
    const res = await fetch(`http://127.0.0.1:5000/api/order/get/${params.orderID}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + locals.accessToken
        }
    })
    const json = await res.json()

    if (!res.ok) error(400, json.message)

    return {order: json.data }
}