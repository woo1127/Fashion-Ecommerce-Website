/** @type {import('./$types').PageServerLoad} */
export function load({ locals }) {
    return {
        user: locals.accessToken || null,
    }
}