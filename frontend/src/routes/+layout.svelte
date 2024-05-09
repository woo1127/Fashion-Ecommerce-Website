<script>
    import '$lib/styles/normalize.css'
    import '$lib/styles/index.css'
    import { afterUpdate } from 'svelte';
    import { page } from '$app/stores'
    import { getFlash } from 'sveltekit-flash-message'

    let active = false
    const flash = getFlash(page, {clearAfterMs: 3500})

    // fallback when clearAfterMs doesn't work, idk why it doesn't work
    afterUpdate(() => {
        if ($flash) {
            setTimeout(() => {
                $flash = null
            }, 3500)
        }
    })
</script>


<nav class="navbar">
    <h1 class="logo">
        <a href="/">LUXE</a>
    </h1>

    <div class="search-container" class:search-container--active={active}>
        <form method="POST" action="/?/search" class="search">
            <input type="text" placeholder="Search"  id="q" name="q" class="search__input">
            <button type="submit" class="search__btn">
                <span class="icon">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M15.7955 15.8111L21 21M18 10.5C18 14.6421 14.6421 18 10.5 18C6.35786 18 3 14.6421 3 10.5C3 6.35786 6.35786 3 10.5 3C14.6421 3 18 6.35786 18 10.5Z" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>                
                </span>
            </button>
        </form>
        <span class="icon" on:click={() => active = false} on:keydown role="button" tabindex="0">
            <svg fill="#000000" viewBox="0 0 200 200" data-name="Layer 1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><title></title><path d="M114,100l49-49a9.9,9.9,0,0,0-14-14L100,86,51,37A9.9,9.9,0,0,0,37,51l49,49L37,149a9.9,9.9,0,0,0,14,14l49-49,49,49a9.9,9.9,0,0,0,14-14Z"></path></g></svg>
        </span>
    </div>

    <div class="navbar-icons">
        <div class="navbar-icons__item" on:click={() => active = true} on:keydown role="button" tabindex="0">
            <span class="icon">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M15.7955 15.8111L21 21M18 10.5C18 14.6421 14.6421 18 10.5 18C6.35786 18 3 14.6421 3 10.5C3 6.35786 6.35786 3 10.5 3C14.6421 3 18 6.35786 18 10.5Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
            </span>
        </div>

        {#if $page.data.user}
            <div class="navbar-icons__item" id="user-icon">
                <span class="icon">
                    <svg class="navbar__icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M16 7C16 9.20914 14.2091 11 12 11C9.79086 11 8 9.20914 8 7C8 4.79086 9.79086 3 12 3C14.2091 3 16 4.79086 16 7Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M12 14C8.13401 14 5 17.134 5 21H19C19 17.134 15.866 14 12 14Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
                </span>
                <div class="dropdown">
                    <div class="dropdown__item">
                        <a href="/user/profile">Profile</a>
                    </div>
                    <div class="dropdown__item">
                        <a href="/user/purchase">Purchase History</a>
                    </div>
                    <div class="dropdown__item">
                        <form method="POST" action="/?/logout">
                            <button type="submit">Logout</button>
                        </form>
                    </div>
                </div>
            </div>
        {:else} 
            <div class="navbar-icons__item">
                <span class="icon">
                    <a href="/auth/login">
                        <svg class="navbar__icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M16 7C16 9.20914 14.2091 11 12 11C9.79086 11 8 9.20914 8 7C8 4.79086 9.79086 3 12 3C14.2091 3 16 4.79086 16 7Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M12 14C8.13401 14 5 17.134 5 21H19C19 17.134 15.866 14 12 14Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
                    </a>
                </span>
            </div>
        {/if}

        <div class="navbar-icons__item">
            <span class="icon" id="cart-icon">
                <a href="/cart">
                    {#if $page.data.cart_item_count !== 0}
                        <span>{$page.data.cart_item_count}</span>
                    {/if}
                    <svg class="navbar__icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M6.29977 5H21L19 12H7.37671M20 16H8L6 3H3M9 20C9 20.5523 8.55228 21 8 21C7.44772 21 7 20.5523 7 20C7 19.4477 7.44772 19 8 19C8.55228 19 9 19.4477 9 20ZM20 20C20 20.5523 19.5523 21 19 21C18.4477 21 18 20.5523 18 20C18 19.4477 18.4477 19 19 19C19.5523 19 20 19.4477 20 20Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
                </a>
            </span>
        </div>
    </div>
</nav>

<div class="page-content">
    {#if $flash}
        <div 
            class="popup"
            class:popup--success={$flash.type === 'success'}
            class:popup--error={$flash.type === 'error'}
        >
            <span class="popup__icon">
                {#if $flash.type == 'success'}
                    <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><defs><style> .cls-1 { fill: #699f4c; fill-rule: evenodd; } </style></defs><path class="cls-1" d="M800,510a30,30,0,1,1,30-30A30,30,0,0,1,800,510Zm-16.986-23.235a3.484,3.484,0,0,1,0-4.9l1.766-1.756a3.185,3.185,0,0,1,4.574.051l3.12,3.237a1.592,1.592,0,0,0,2.311,0l15.9-16.39a3.187,3.187,0,0,1,4.6-.027L817,468.714a3.482,3.482,0,0,1,0,4.846l-21.109,21.451a3.185,3.185,0,0,1-4.552.03Z" id="check" transform="translate(-770 -450)"></path></g></svg>
                {:else}
                    <svg fill="#ff424f" viewBox="0 0 200 200" data-name="Layer 1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" stroke="#ff424f"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><title></title><path d="M100,15a85,85,0,1,0,85,85A84.93,84.93,0,0,0,100,15Zm0,150a65,65,0,1,1,65-65A64.87,64.87,0,0,1,100,165Z"></path><path d="M128.5,74a9.67,9.67,0,0,0-14,0L100,88.5l-14-14a9.9,9.9,0,0,0-14,14l14,14-14,14a9.9,9.9,0,0,0,14,14l14-14,14,14a9.9,9.9,0,0,0,14-14l-14-14,14-14A10.77,10.77,0,0,0,128.5,74Z"></path></g></svg>
                {/if}
            </span>
            <p class="popup__text">{$flash.message}</p>
        </div>
    {/if}
    <slot />
</div>

<!-- <footer class="footer">
    Footer 
</footer> -->


<style>
    .page-content {
        position: relative;
        min-height: 90vh;
        margin-top: 10vh;
    }
    .navbar {
        width: 100%;
        height: 10vh;
        position: fixed;
        inset: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        background-color: #fff;
        box-shadow: 0 1px 4px 0 rgba(74, 74, 78, .12);
    }
    .logo {
        font-size: 3.2rem;
        letter-spacing: 2px;
    }
    .navbar-icons {
        position: absolute;
        top: 0;
        right: 0;
        height: 100%;
        display: flex;
        padding-right: 5rem;
    }
    .navbar-icons__item {
        display: inline-flex;
        justify-items: center;
        align-items: center;
        height: 100%;
        padding-inline: 2.5rem;
        cursor: pointer;
    }
    .icon {
        padding: 4px;
        width: 32px;
        height: 32px;
        cursor: pointer;
    }

    #cart-icon {
        position: relative;
    }
    #cart-icon span {
        position: absolute;
        display: inline-flex;
        justify-content: center;
        align-items: center;
        font-size: 1.1rem;
        top: -3px;
        right: -6px;
        width: 16px;
        height: 16px;
        background-color: red;
        border-radius: 50%;
        color: #fff;
    }

    .search-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 3rem;
        height: 10vh;
        position: absolute;
        z-index: 1001;
        inset: 0;
        transform: translateY(-100%);
        background-color: #fff;
        transition: all .3s cubic-bezier(.39,.575,.565,1);
    }
    .search-container--active {
        transform: translateY(0);
    }
    .search {
        width: 60vw;
        display: flex;
        justify-content: space-between;
        border: 1px solid var(--primary-line-color);
        border-radius: 3px;
    }
    .search__input {
        border: none;
        outline: none;
        flex: 1;
        margin: 1rem 2rem;
    }
    .search__btn {
        background-color: var(--primary-color);
        border: none;
        border-radius: 3px;
        color: #fff;
        display: inline-flex;
        justify-content: center;
        align-items: center;
        padding-inline: 2rem;
    }

    #user-icon {
        position: relative;
    }
    #user-icon:hover > .dropdown {
        display: flex;
        padding: 1rem 0;
    }
    .dropdown {
        position: absolute;
        top: 10vh;
        left: 50%;
        transform: translateX(-50%);
        display: none;
        flex-direction: column;
        background-color: #fff;
        border: 1px solid var(--primary-line-color);
    }
    .dropdown__item {
        width: 200px;
        white-space: nowrap;
        transition: all .15s ease-in-out;
    }
    .dropdown__item > a,
    .dropdown__item > form > button {
        width: 100%;
        display: block;
        padding: 1rem 0 1rem 3rem;
        text-align: left
    }
    .dropdown__item:hover {
        background-color: #f5f5f5;
        color: var(--primary-color);
    }
    .dropdown__item button {
        border: none;
        outline: none;
        background-color: inherit;
    }

    @keyframes updown {
        0% {
            top: -50vh;
        }
        35% {
            top: 20vh;
        }
        65% {
            top: 20vh;
        }
        100% {
            top: -50vh;
        }
    }
    .popup {
        position: absolute;
        left: 50%;
        transform: translate(-50%, -50%);
        opacity: 0.95;
        z-index: 500;
        padding: 3.5rem 3rem;
        border-radius: 5px;
        display: flex;
        flex-direction: column;
        place-items: center;
        display: flex;
        flex-direction: column;
        place-items: center;
        animation: updown 3500ms ease-in-out;
    }
    .popup__icon {
        display: inline-grid;
        place-items: center;
        width: 42px;
        height: 42px;
        padding-bottom: 3.2rem;
    }
    .popup__text {
        font-size: 1.6rem;
    }
    .popup--success {
        color: #4F8A10;
        background-color: #DFF2BF;
        border: 2px solid #d4f39e;
    }
    .popup--error {
        color: #D8000C;
        background-color: #FFBABA;
        border: 2px solid #fc9595;
    }
</style>