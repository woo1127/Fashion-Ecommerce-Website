<script>
    import { page } from '$app/stores'
    import { enhance } from '$app/forms'

    /** @type {import('./$types').ActionData} */
    export let form;

    // This variable need to be reactive so that page will be re-rendered 
    // when the redirect function been called at the +page.server.js
    $: authType = $page.params.authType
</script>

<svelte:head>
    <title>{authType} | LUXE Malaysia</title>
</svelte:head>

<div class="page-content">
    <section class="form-container">
        <div class="form-container__header">
            {#if authType === 'login'}
                <h2>Login</h2>
            {:else if authType === 'signup'}
                <h2>Sign Up</h2>
            {/if}
        </div>
        <div class="form-container__body">
            {#if authType === 'login'}
                <form method="POST" action="?/login" use:enhance>
                    {#if form?.error}
                        <div class="error">
                            <div class="error__icon-container">
                                <svg fill="#ff424f" viewBox="0 0 200 200" data-name="Layer 1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" stroke="#ff424f"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><title></title><path d="M100,15a85,85,0,1,0,85,85A84.93,84.93,0,0,0,100,15Zm0,150a65,65,0,1,1,65-65A64.87,64.87,0,0,1,100,165Z"></path><path d="M128.5,74a9.67,9.67,0,0,0-14,0L100,88.5l-14-14a9.9,9.9,0,0,0-14,14l14,14-14,14a9.9,9.9,0,0,0,14,14l14-14,14,14a9.9,9.9,0,0,0,14-14l-14-14,14-14A10.77,10.77,0,0,0,128.5,74Z"></path></g></svg>
                            </div>
                            <div class="error__message">{form?.message}</div>
                        </div>
                    {/if}
                    <div class="form__input-group">
                        <input class="form__input" type="email" id="email" name="email" placeholder=" " required />
                        <label class="form__label" for="email">Email *</label>
                    </div>
                    <div class="form__input-group">
                        <input class="form__input" type="password" id="password" name="password" autocomplete="off" placeholder=" " required />
                        <label class="form__label" for="password">Password *</label>
                    </div>
                    <button type="submit" class="form__btn">Log In</button>
                </form>
                <div class="separator">
                    <div class="separator__line"></div>
                    <span class="separator__text">OR</span>
                    <div class="separator__line"></div>
                </div>
                <div class="alternative-container">
                    <p>New to Luxe?</p>
                    <a rel="external" href="/auth/signup">Sign Up</a>
                </div>
            {:else if authType === 'signup'}
                <form method="POST" action="?/signup" use:enhance>
                    {#if form?.error}
                        <div class="error">
                            <div class="error__icon-container">
                                <svg fill="#ff424f" viewBox="0 0 200 200" data-name="Layer 1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" stroke="#ff424f"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><title></title><path d="M100,15a85,85,0,1,0,85,85A84.93,84.93,0,0,0,100,15Zm0,150a65,65,0,1,1,65-65A64.87,64.87,0,0,1,100,165Z"></path><path d="M128.5,74a9.67,9.67,0,0,0-14,0L100,88.5l-14-14a9.9,9.9,0,0,0-14,14l14,14-14,14a9.9,9.9,0,0,0,14,14l14-14,14,14a9.9,9.9,0,0,0,14-14l-14-14,14-14A10.77,10.77,0,0,0,128.5,74Z"></path></g></svg>
                            </div>
                            <div class="error__message">{form?.message}</div>
                        </div>
                    {/if}
                    <div class="form__input-group">
                        <input type="text" class="form__input" id="username" name="username" placeholder=" " required />
                        <label for="username" class="form__label">Username *</label>
                    </div>
                    <div class="form__input-group">
                        <input class="form__input" type="email" id="email" name="email" autocomplete="off" placeholder=" " required />
                        <label class="form__label" for="email">Email *</label>
                    </div>
                    <div class="form__input-group">
                        <input class="form__input" type="password" id="password" name="password" autocomplete="off" placeholder=" " required />
                        <label class="form__label" for="password">Password *</label>
                    </div>
                    <div class="form__input-group">
                        <input class="form__input" type="tel" id="phone" name="phone" autocomplete="off" placeholder=" " required />
                        <label class="form__label" for="phone">Phone number *</label>
                    </div>
                    <button class="form__btn">Sign Up</button>
                </form>
                <div class="separator">
                    <div class="separator__line"></div>
                    <span class="separator__text">OR</span>
                    <div class="separator__line"></div>
                </div>
                <div class="alternative-container">
                    <p>Have an account?</p>
                    <a rel="external" href="/auth/login">Login</a>
                </div>
            {/if}
        </div>
    </section>
</div>

<style>
    .page-content {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .form-container {
        display: flex;
        flex-direction: column;
        width: 70%;
        margin: 3rem auto;
    }
    .form-container__header {
        background-color: #fff;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        margin-bottom: 2px;
        border-radius: 3px 3px 0 0;
    }
    .form-container__header > h2 {
        font-size: 2rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        padding: 2rem 4rem;
    }
    .form-container__body {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        width: 100%;
        background-color: #fff;
        border-radius: 0 0 3px 3px;
        padding-top: 3rem;
    }
    .form-container__body > * {
        width: 50%;
        margin-bottom: 3rem;
    }
    .form-container__body form {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .form__input-group {
        margin-inline: auto;
        margin-bottom: 2.6rem;
        position: relative;
        width: 100%;
        height: 4.5rem;
    }
    .form__input {
        position: absolute;
        inset: 0;
        background: none;
        outline: none;
        padding-inline: 1.5rem;
        border: 1px solid var(--primary-line-color);
        border-radius: 3px;
        transition: all 160ms ease-in;
    }
    .form__input:hover {
        border-color: var(--secondary-color);
    }
    .form__input:focus {
        border-color: var(--secondary-color--decent);
    }
    .form__label {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        left: 1rem;
        padding: 0 0.5rem;
        color: var(--fc-secodary);
        background-color: #fff;
        cursor: text;
        transition: top 200ms ease-in, left 200ms ease-in, font-size 200ms ease-in;
    }
    .form__input:focus ~ .form__label,
    .form__input:not(:placeholder-shown).form__input:not(:focus) ~ .form__label{
        top: 0;
        font-size: 1.2rem;
        font-weight: 600;
        color: #333;
    }
    .form__btn {
        margin-inline: auto;
        height: 3.8rem;
        width: 50%;
        background-color: var(--primary-color);
        border: none;
        border-radius: 3px;
        outline: none;
        color: #fff;
        font-size: 1.6rem;
    }
    .separator {
        display: flex;
        align-items: center;
        justify-content: space-evenly;
    }
    .separator__line {
        width: 100%;
        height: 1px;
        background-color: var(--primary-line-color);
    }
    .separator__text {
        padding: 0 1rem;
        background-color: #fff;
        font-size: 1.4rem;
        color: var(--fc-secodary);
    }
    .alternative-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 2rem;
    }
    .alternative-container > p {
        color: var(--fc-secodary);
    }
    .alternative-container > a {
        color: var(--fc-primary-color);
        font-weight: 700;
    }
    .error {
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1.2rem 1.5rem;
        margin-bottom: 2.6rem;
        background-color: #fff9fa;
        border: 1px solid rgba(255, 66, 79, .2);
        border-radius: 3px;
    }
    .error__icon-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-right: 1.5rem;
    }
    .error__icon-container > svg {
        width: 24px;
        height: 24px;
    }
</style>