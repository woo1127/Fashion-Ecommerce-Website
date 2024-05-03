/** @type {import('@sveltejs/kit').Handle} */
export function handle({ event, resolve }) {
	const accessToken = event.cookies.get('access_token')
	const userID = event.cookies.get('user_id')

	event.locals.accessToken = accessToken
	event.locals.userID = userID

	return resolve(event)
}