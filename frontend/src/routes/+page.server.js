import { redirect } from '@sveltejs/kit'

/** @type {import('./$types').Actions} */
export const actions = {
    search: async ({ url, request }) => {
        const formData = await request.formData()
        
        url.searchParams.set('q', formData.get('q'))
        url.searchParams.set('page', '1')

        // console.log(url)

        throw redirect(303, `/search?${url.searchParams.toString()}`)
    },

    logout: async ({ cookies }) => {
        cookies.set('access_token', '', {
            path: '/',
            expires: new Date(0),
        })
        cookies.set('user_id', '', {
            path: '/',
            expires: new Date(0),
        })
        
        throw redirect(303, '/auth/login')
    }
}