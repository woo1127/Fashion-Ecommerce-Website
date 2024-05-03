import { error } from '@sveltejs/kit'

/** @type {import('./$types').PageServerLoad} */
export async function load({ locals }) {
    const res = await fetch('http://127.0.0.1:5000/api/order/list', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${locals.accessToken}` 
        }
    })
    const json = await res.json()

    if (!res.ok) error(json.code, json.message)

    return {
        orders: json.data,
        access_token: locals.accessToken
    }
}