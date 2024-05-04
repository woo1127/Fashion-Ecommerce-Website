import { redirect } from '@sveltejs/kit'

const public_paths = [
	'/search',
	'/product',
	'/auth/signup',
	'/auth/login',
];

function isPathAllowed(path) {
	return public_paths.some(allowedPath =>
		path === allowedPath || path.startsWith(allowedPath + '/') || path === '/__data.json'
	);
}

/** @type {import('@sveltejs/kit').Handle} */
export async function handle({ event, resolve }) {
	let accessToken = null
	let userID = null

	if (
		event.cookies.get('access_token') != undefined && event.cookies.get('access_token') != null &&
		event.cookies.get('user_id') != undefined && event.cookies.get('user_id') != null
	) { 
		accessToken = event.cookies.get('access_token')
		userID = event.cookies.get('user_id')
	}

	const url = new URL(event.request.url)

	if (!accessToken && !userID && !isPathAllowed(url.pathname)) {
		throw redirect(302, '/auth/login')
	}

	if (accessToken && userID) {
		event.locals.accessToken = accessToken
		event.locals.userID = userID
		
		if (url.pathname === '/auth/login' || url.pathname === '/auth/signup') {
			throw redirect(302, '/')
		}
	}

	const response = await resolve(event)
	return response
}