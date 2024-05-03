<script>
    import ButtonGroup from '$lib/components/ButtonGroup.svelte';
    import { browser } from '$app/environment';
    import { goto } from '$app/navigation';

    /** @type {import('./$types').PageData} */
    export let data
    
    let { carts, access_token } = data;
    let totalPrice = carts.reduce((acc, cart) => acc + cart.total_price, 0);
    let payments = {
        "values": [],
        "methods": ["Credit / Debit Card", "Online Banking", "Cash On Delivery", "Paypal", "Apply Pay", "Google Pay"]
    }

    async function placeOrder() {
        if (payments.values.length === 0) {
            alert('Please select a payment method')
            return
        }

        const res = await fetch('http://127.0.0.1:5000/api/order/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + access_token
            },
            body: JSON.stringify({
                'cart_ids': carts.map(cart => cart.id),
                'payment_method': payments.values[0]
            })
        })
        const json = await res.json()

        if (!res.ok) throw new Error(data.message)

        goto('/checkout/success/' + json.data.id)
    }

    console.log(carts)
    console.log(totalPrice)
</script>

<svelte:head>
    <title>Checkout | LUXE Malaysia</title>
</svelte:head>

<div class="page-content">
    <section class="container">
        <section class="left-container">
            <div class="title">
                Checkout
            </div>
            <div class="card">
                <div class="card__header">
                    Delivery Address
                </div>
                <div class="card__content">
                    <div class="address-container">
                        <div class="address__info">
                            <p class="address__name">Jeremy</p>
                            <p class="address__phone">0123456780</p>
                            <p class="address__text">88, Persiaran Relau, Jalan Rumbia, 11900 Pulau Pinang</p>
                        </div>
                        <button id="change-address-btn">Change</button>
                    </div>
                </div>
            </div>
            <div class="card">
                <div class="card__header">Payment Method</div>
                <div class="card__content">
                    <ButtonGroup
                        bind:values={payments.values}
                        let:values
                        let:selectButton
                    >
                        <div class="payment-list">
                            {#each payments.methods as method}
                                <button 
                                    class="payment-list__item"
                                    class:active={values.includes(method)}
                                    on:click={() => selectButton(method)}
                                >
                                    {method}
                                </button>
                            {/each}
                        </div>
                    </ButtonGroup>
                </div>
            </div>
        </section>

        <aside class="right-container">
            <div class="cart">
                <div class="cart-header">
                    <h2 class="header__title">My Shopping Cart</h2>
                    <a href="/cart">Modify Shopping Cart</a>
                </div>
                <div class="cart-list">
                    {#each carts as cart (cart.id)}
                        <div class="cart-item">
                            <div class="cart-item__image">
                                <picture>
                                    <img src={cart.color_detail.url} alt="" loading="lazy">
                                </picture>
                            </div>
                            <div class="cart-item__info">
                                <h3 class="item-name">{cart.product_detail.name}</h3>
                                <p class="item-price">S$ {cart.total_price}</p>
                            </div>
                        </div>
                    {/each}
                </div>

                <div class="cart-footer">
                    <div class="price-container">
                        <p class="price__text">Subtotal</p>
                        <p class="price__value">S$ {totalPrice}</p>
                    </div>
                    <div class="price-container">
                        <p class="price__text">Shipping</p>
                        <p class="price__value">S$ 0</p>
                    </div>
                    <div class="price-container--big">
                        <p class="price__text--big">Total</p>
                        <p class="price__value--big">S$ {totalPrice}</p>
                    </div>
                    <button on:click={placeOrder} disabled={carts.length === 0} id="place-order-btn">Place Order</button>
                </div>
            </div>
        </aside>
    </section>
</div>


<style>
    .container {
        display: flex;
    }
    .left-container {
        padding: 4rem 6rem;
        width: 67%;
    }
    .title {
        padding: 0 1rem 2.5rem 1rem;
        font-size: 2.5rem;
        font-weight: 700;
    }
    .card {
        background: #fff;
        border-radius: 3px;
        box-shadow: 0 1px 1px 0 rgba(0, 0, 0, .05);
        margin-bottom: 3rem;
    }
    .card__header {
        padding: 2rem 3rem;
        font-size: 2.1rem;
        font-weight: 600;
        border-bottom: 1px solid var(--primary-line-color);
    }
    .card__content {
        padding: 3rem;
    }
    .address-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .address__info {
        display: flex;
        align-items: center;
    }
    .address__name {
        font-weight: 600;
        padding-right: 1rem;
    }
    .address__phone {
        font-weight: 600;
        padding-right: 2rem;
    }
    .payment-list {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
    }
    .payment-list__item {
        position: relative;
        padding: 0.8rem 1.6rem;
        border-radius: 2px;
        border: 1px solid var(--primary-line-color);
        transition: all .15s ease-in-out;
    }
    .payment-list__item:hover,
    .payment-list__item.active {
        background-color: var(--primary-color);
        color: #fff;
        border: 1px solid var(--primary-color);
    }
    .payment-list__item:hover::after,
    .payment-list__item.active::after {
        content: "";
        position: absolute;
        top: -5px;
        left: -5px;
        width: calc(100% + 10px);
        height: calc(100% + 10px);
        border: 2px solid var(--primary-color);
    }
    #place-order-btn {
        background-color: var(--primary-color);
        color: #fff;
        border-radius: 3px;
        padding: 1.2rem 0;
        border: 2px solid var(--primary-color);
        width: 100%;
    }
    #change-address-btn {
        background-color: var(--primary-color);
        color: #fff;
        padding: 0.4rem 1.2rem;
        border: none;
        border-radius: 3px;
    }
    .right-container {
        background: #fff;
        width: 33%;
    }
    .cart {
        padding: 2.5rem;
        padding-top: 4rem;
    }
    .cart-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-inline: 1.2rem;
        padding-bottom: 3rem;
    }
    .cart-header > .header__title {
        font-size: 1.6rem;
        font-weight: 600;
    }
    .cart-header > a {
        text-decoration: underline;
    }
    .cart-item {
        display: flex;
        padding: 1.2rem 1.2rem 1.2rem 0;
        border-bottom: 1px solid var(--primary-line-color);
    }
    .cart-item__image {
        width: 80px;
        height: auto;
        aspect-ratio: 1/1;
    }
    .cart-item__info {
        padding-left: 2rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .cart-item__info > .item-name {
        font-size: 1.4rem;
        font-weight: 500;
        padding-bottom: 0.8rem;
    }
    .cart-footer {
        padding: 3rem 0;
    }
    .price-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 1.4rem;
    }
    .price__text {
        text-align: left;
    }
    .price__value {
        text-align: right;
        font-size: 1.5rem;
    }
    .price-container--big {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.4rem 0 2.8rem 0;
    }
    .price__text--big {
        font-size: 1.7rem;
        font-weight: 500;
    }
    .price__value--big {
        font-size: 1.9rem;
        font-weight: 500;
    }
</style>