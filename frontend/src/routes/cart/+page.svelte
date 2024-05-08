<script>
    import { goto, invalidateAll } from '$app/navigation'

    /** @type {import('./$types').PageData} */
    export let data

    let { carts, access_token } = data;
    $: totalPrice = carts.reduce((acc, cart) => acc + cart.total_price, 0);


    async function updateQuantity(cartId, newQuantity) {
        const res = await fetch("http://127.0.0.1:5000/api/cart/update", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + access_token
            },
            body: JSON.stringify({
                cart_id: cartId,
                update_fields: {
                    quantity: newQuantity,
                    total_price: newQuantity * carts.find(cart => cart.id == cartId).product_detail.price
                }
            })
        })
        const json = await res.json()

        if (!res.ok) throw new Error(json.message)

        // filter and update the corresponding item in the carts array
        carts = carts.map(cart => {
            if (cart.id === cartId) return {...json.data}
            else return cart
        })
    }


    async function deleteItem(cartId) {
        const res = await fetch("http://127.0.0.1:5000/api/cart/delete", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + access_token
            },
            body: JSON.stringify({
                cart_id: cartId
            })
        })
        const json = await res.json()

        if (!res.ok) throw new Error(json.message)

        carts = carts.filter(cart => cart.id !== cartId)

        // reload the page to update the cart item count
        invalidateAll('/cart')
    }
</script>

<svelte:head>
    <title>Shopping Cart | LUXE Malaysia</title>
</svelte:head>

<div class="page-content">
    <section class="container">
        <section class="left-container">
            <div class="title-header">
                <div class="title-header__text">My Shopping Cart</div>
                <a href="/">Continue to shopping</a>
            </div>
            {#each carts as cart (cart.id)}
                <div class="product">
                    <div class="product-image">
                        <picture>
                            <img src={cart.color_detail.url} alt="" loading="lazy">
                        </picture>
                    </div>
                    <div class="product-info">
                        <div class="product-name">
                            <h2>{cart.product_detail.name}</h2>
                            <span class="delete-btn" on:click={() => deleteItem(cart.id)} on:keydown role="button" tabindex="0">
                                <svg viewBox="0 0 1024 1024" fill="#ff424f" version="1.1" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M332 663.2c-9.6 9.6-9.6 25.6 0 35.2s25.6 9.6 35.2 0l349.6-356c9.6-9.6 9.6-25.6 0-35.2s-25.6-9.6-35.2 0L332 663.2z" fill=""></path><path d="M681.6 698.4c9.6 9.6 25.6 9.6 35.2 0s9.6-25.6 0-35.2L367.2 307.2c-9.6-9.6-25.6-9.6-35.2 0s-9.6 25.6 0 35.2l349.6 356z" fill=""></path><path d="M516.8 1014.4c-277.6 0-503.2-225.6-503.2-503.2S239.2 7.2 516.8 7.2s503.2 225.6 503.2 503.2-225.6 504-503.2 504z m0-959.2c-251.2 0-455.2 204.8-455.2 456s204 455.2 455.2 455.2 455.2-204 455.2-455.2-204-456-455.2-456z" fill=""></path></g></svg>
                            </span>
                        </div>
                        <div class="product-attributes">
                            <div class="field">
                                <div class="field__title">Color</div>
                                {#if !cart.color_detail.secondary_color}
                                    <div class="field__value">{cart.color_detail.primary_color}</div>
                                {:else}
                                    <div class="field__value">{cart.color_detail.primary_color} / {cart.color_detail.secondary_color}</div>
                                {/if}
                            </div>
                            <div class="field">
                                <div class="field__title">Size</div>
                                <div class="field__value">{cart.size_detail.value}</div>
                            </div>
                            <div class="field">
                                <div class="field__title">Unit Price</div>
                                <div class="field__value">S$ {cart.product_detail.price}</div>
                            </div>
                            <div class="field">
                                <div class="field__title">Quantity</div>
                                <div class="field__value">
                                    <div class="counter-group">
                                        <button on:click={() => updateQuantity(cart.id, --cart.quantity)}>
                                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M6 12L18 12" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
                                        </button>
                                        <input type="text" value={cart.quantity}>
                                        <button on:click={() => updateQuantity(cart.id, ++cart.quantity)}>
                                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M4 12H20M12 4V20" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="product-total">
                            <div class="field">
                                <div class="field__title--big">SubTotal :</div>
                                <div class="field__value--big">S$ {cart.total_price}</div>
                            </div>
                        </div>
                    </div>
                </div>
            {/each}
        </section>
        <aside class="right-container">
            <div class="field">
                <div class="field__title">Subtotal :</div>
                <div class="field__value">S$ {totalPrice}</div>
            </div>
            <div class="field">
                <div class="field__title">Shipping</div>
                <div class="field__value">S$ 0</div>
            </div>
            <div class="field field--big">
                <div class="field__title--big">Total</div>
                <div class="field__value--big">S$ {totalPrice}</div>
            </div>
            <button class="checkout-btn" disabled={carts.length === 0} on:click={() => goto('/checkout')}>
                Checkout Now
            </button>
        </aside>
    </section>
</div>


<style>
    .container {
        position: relative;
        display: flex;
    }
    .left-container {
        padding: 4rem 6rem;
        width: 70%;
    }
    .right-container {
        position: absolute;
        top: 0;
        right: 0;
        min-height: 100vh;
        width: 30%;
        background-color: #fff;
        padding-top: 14rem;
        padding-inline: 3rem;
    }
    .title-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        padding: 0 1rem 2.5rem 1rem;
    }
    .title-header__text {
        font-size: 2.5rem;
        font-weight: 700;
    }
    .title-header > a {
        text-decoration: underline;
    }
    .product {
        display: flex;
        height: 70vh;
        background-color: #fff;
        box-shadow: 0 1px 1px 0 rgba(0, 0, 0, .05);
        border-radius: 3px;
        margin-bottom: 3rem;
    }
    .product-image {
        flex: 1;
        padding: 1rem;
    }
    .product-info {
        flex: 1;
        display: flex;
        flex-direction: column;
    }
    .product-name,
    .product-attributes,
    .product-total {
        padding: 3rem;
        border-left: 1px solid var(--primary-line-color);
    }
    .product-name {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid var(--primary-line-color);
    }
    .product-name > h2 {
        font-size: 1.8rem;
        padding-right: 1.5rem;
    }
    .product-name > .delete-btn {
        width: 28px;
        height: 28px;
        padding: 4px;
        cursor: pointer;
    }
    .product-attributes {
        flex: 1;
        border-bottom: 1px solid var(--primary-line-color);
    }
    .product-total > .field {
        margin: 0;
    }
    .counter-group {
        display: flex;
        border: 1px solid var(--primary-line-color);
    }
    .counter-group > input {
        width: 5rem;
        text-align: center;
        border: none;
    }
    .counter-group > button {
        padding: 0.4rem 0.8rem;
        border: none;
    }
    .counter-group > button:first-child {
        border-right: 1px solid var(--primary-line-color);
    }
    .counter-group > button:last-child {
        border-left: 1px solid var(--primary-line-color);
    }
    .counter-group svg {
        width: 12px;
        height: 12px;
    }
    .field {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.4rem;
    }
    .field__title {
        text-align: left;
    }
    .field__value {
        text-align: right;
    }
    .field__title--big {
        font-size: 1.7rem;
        font-weight: 500;
    }
    .field__value--big {
        font-size: 1.9rem;
        font-weight: 500;
    }
    .right-container .field--big {
        margin: 3.5rem 0;
    }
    .right-container .field__value {
        font-size: 1.7rem;
    }
    .checkout-btn {
        background-color: var(--primary-color);
        color: #fff;
        border-radius: 3px;
        padding: 1.2rem 0;
        border: 2px solid var(--primary-color);
        width: 100%;
    }
</style>