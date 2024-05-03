import { fail, redirect } from '@sveltejs/kit';


/** @type {import('./$types').PageServerLoad} */
export async function load({ locals }) {
	if (locals.accessToken) throw redirect(307, '/');
}

export const actions = {
    login: async ({ request, cookies }) => {
        const formData = await request.formData();
        const data = {
            email: formData.get('email'),
            password: formData.get('password'),
        }

        const res = await fetch('http://127.0.0.1:5000/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        })
        const json = await res.json();

        if (!res.ok) 
            return fail(400, { message: json.message, error: true })

        const options = {
            path: '/',
            httpOnly: true,
            maxAge: 60 * 60 * 24 * 90,
        }

        cookies.set('user_id', json.data.user_id, options);
        cookies.set('access_token', json.data.access_token, options);

        redirect(303, '/')
    },

    signup: async ({ request }) => {
        const formData = await request.formData();
        const data = {
            username: formData.get('username'),
            email: formData.get('email'),
            password: formData.get('password'),
            phone_number: formData.get('phone'),
        }

        const res = await fetch('http://127.0.0.1:5000/api/auth/signup', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        })
        const json = await res.json();
        
        if (!res.ok) 
            return fail(json.code, { message: json.message, error: true })

        throw redirect(303, '/auth/login')
    }
}