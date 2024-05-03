/** @type {import('./$types').PageServerLoad} */
export async function load({ url, fetch }) {
    const urlParams = url.searchParams
    const result = async () => {
        const res = await fetch(`http://127.0.0.1:5000/api/product/search?${urlParams}`)
        return await res.json()
    }
    return { result: result() }
}