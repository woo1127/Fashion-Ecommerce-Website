<script>
    import ButtonGroup from '$lib/components/ButtonGroup.svelte';	
        
    /** @type {import('./$types').PageData} */
    export let data
    let { product, access_token, user_id } = data
    let imageURLs = [
        ...product.images.map(({url}) => url), 
        ...product.colors.map(({url}) => url)
    ].slice(1)
    let activeImage = imageURLs[0]
    let options = {images: [], sizes: [], colors: [], quantity: 1}

    console.log(access_token)
    

    async function addToCart() {
        if (options.sizes.length === 0 || options.colors.length === 0) {
            alert('Please select all product variations')
            return
        }

        if (!access_token)
            alert('Please login to add to cart or purchase')

        const res = await fetch('http://127.0.0.1:5000/api/cart/add', {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + access_token,
            },
            body: JSON.stringify({
                user_id,
                product_id: product.id,
                size_id: options.sizes[0],
                color_id: options.colors[0],
                quantity: options.quantity,
                total_price: product.price * options.quantity
            })
        })

        if (res.ok)
            alert('Item successfully added to cart')
    }
</script>

<svelte:head>
    <title>{product.name} | LUXE Malaysia</title>
</svelte:head>

<section class="container">
    <div class="product card">
        <section class="product-images">
            <div class="product-images__header">
                <picture>
                    <img loading="lazy" src="{activeImage}" alt="">
                </picture>
            </div>
            <ButtonGroup
                bind:values={options.images}
                let:values
                let:selectButton
            >
                <div class="product-images__list">
                    {#each imageURLs as url}
                        <button 
                            on:click={() => activeImage = url} 
                            on:click={() => selectButton(url)}
                            on:mouseenter={() => activeImage = url}
                            on:mouseenter={() => selectButton(url)}
                            class="product-images__list-item"
                            class:active={activeImage === url}
                        >
                            <picture>
                                <img loading="lazy" src={url} alt="" />
                            </picture>
                        </button>
                    {/each}
                </div>
            </ButtonGroup>
        </section>
        <section class="product-info">
            <h1 class="product__name">{product.name}</h1>
            <p class="product__price">S$ {product.price}</p>
            <div class="separator"></div>
            <div class="product-color-container">
                <p class="product-color-title">Color</p>
                <ButtonGroup 
                    bind:values={options.colors}
                    let:values
                    let:selectButton
                >
                    <div class="product-color-list">
                        {#each product.colors as color}
                            {#if color.secondary_color === null}
                                <button 
                                    class:active={values.includes(color.id)} 
                                    class="product-color-list__item" 
                                    on:click={() => selectButton(color.id)} 
                                    on:click={() => activeImage = color.url}
                                    style:background-color={color.primary_color}
                                >
                                </button>
                            {:else if color.secondary_color !== null}
                                <button 
                                    class:active={values.includes(color.id)} 
                                    class="product-color-list__item--multiple product-color-list__item" 
                                    on:click={() => selectButton(color.id)} 
                                    on:click={() => activeImage = color.url}
                                >
                                    <span style:background-color={color.primary_color}></span>
                                    <span style:background-color={color.secondary_color}></span>
                                </button>
                            {/if}
                        {/each}
                    </div>
                </ButtonGroup>
            </div>
            <div class="product-size-container">
                <p class="product-size-title">Size</p>
                <ButtonGroup 
                    bind:values={options.sizes}
                    let:values
                    let:selectButton
                >
                    <div class="product-size-list">
                        {#each product.sizes as size}
                            <button 
                                class:active={values.includes(size.id)} 
                                class="product-size-list__item" 
                                on:click={() => selectButton(size.id)} 
                            >
                                {size.value}
                            </button>
                        {/each}
                    </div>
                </ButtonGroup>
            </div>
            <div class="product-quantity-container">
                <p class="product-quantity-title">Quantity</p>
                <div class="quantity-button-container">
                    <button 
                        class="quantity-button__minus"
                        disabled={options.quantity === 1}
                        on:click={() => options.quantity--}
                    >
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M6 12L18 12" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
                    </button>
                    <input type="number" bind:value={options.quantity} on:input={() => options.quantity = options.quantity > 10 || options.quantity === null ? 10 : options.quantity} />
                    <button 
                        class="quantity-button__plus"
                        disabled={options.quantity === 10}
                        on:click={() => options.quantity++}
                    >
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M4 12H20M12 4V20" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
                    </button>
                </div>
            </div>

            <div class="order-button-container">
                <button class="order-button--primary" on:click={addToCart}>
                    Add to Cart
                </button>
                <button class="order-button--secondary">Purchase Now</button>
            </div>
        </section>
    </div>
</section>


<style>
    .container {
        padding: 2rem 3rem;
    }
    .separator {
        width: 100%;
        height: 2px;
        background-color: var(--bg-color);
        margin: 4.5rem 0;
    }
    .card {
        box-shadow: 0 1px 1px 0 rgba(0, 0, 0, .05);
        border-radius: 3px;
        background-color: #fff;
        margin-bottom: 1rem;
        padding: 1.5rem;
    }
    .product {
        display: flex;
        gap: 6rem;
        padding-bottom: 3rem;
    }
    .product-images__header {
        width: 100%;
        height: 60vh;
        margin-bottom: 1.5rem;
    }
    .product-images__list {
        display: grid;
        grid-template-columns: repeat(5, 84px);
        align-items: stretch;
        justify-content: center;
        gap: 7px;
    }
    .product-images__list-item {
        aspect-ratio: 1/1;
        border: 1px solid var(--primary-line-color);
        transition: all .15s ease-in-out;
    }
    .product-images__list-item:hover, 
    .product-images__list-item.active {
        border: 2px solid var(--primary-color);
    }   
    .product-info {
        flex: 1;
        padding-right: 5rem;
    }
    .product__name {
        font-size: 4.5rem;
        font-weight: 700;
        margin-bottom: 2.5rem;
    }
    .product__price {
        font-size: 2.5rem;
        font-weight: 700;
    }
    .product-size-container {
        display: flex;
        margin-bottom: 4rem;
    }
    .product-size-title {
        width: 13rem;
        margin-top: 1rem;
    }
    .product-size-list {
        display: grid;
        grid-template-columns: repeat(4, max(108px, 15%));
        gap: 12px;
    }
    .product-size-list__item {
        position: relative;
        padding: 1rem 3rem;
        border-radius: 2px;
        border: 1px solid var(--primary-line-color);
        transition: all .15s ease-in-out;
    }
    .product-size-list__item:hover,
    .product-size-list__item.active {
        background-color: var(--primary-color);
        color: #fff;
        border: 1px solid var(--primary-color);
    }
    .product-size-list__item:hover::after,
    .product-size-list__item.active::after {
        content: "";
        position: absolute;
        top: -5px;
        left: -5px;
        width: calc(100% + 10px);
        height: calc(100% + 10px);
        border: 2px solid var(--primary-color);
    }
    .product-color-container {
        display: flex;
        align-items: center;
        margin-bottom: 4rem;
    }
    .product-color-title {
        width: 13rem;
    }
    .product-color-list {
        display: grid;
        grid-template-columns: repeat(6, 36px);
        gap: 12px;
    }
    .product-color-list__item {
        position: relative;
        aspect-ratio: 1/1;
        border: 1px solid var(--primary-line-color);
        transition: all .15s ease-in-out;
    }
    .product-color-list__item--multiple {
        display: flex;
    }
    .product-color-list__item--multiple > span {
        width: 100%;
        height: 100%;
    }
    .product-color-list__item:hover,
    .product-color-list__item.active {
        border: 1px solid var(--primary-color);
    }
    .product-color-list__item:hover::after,
    .product-color-list__item.active::after {
        content: "";
        position: absolute;
        top: -5px;
        left: -5px;
        width: calc(100% + 10px);
        height: calc(100% + 10px);
        border: 2px solid var(--primary-color);
    }
    .product-quantity-container {
        display: flex;
        align-items: center;
        margin-bottom: 4rem;
    }
    .product-quantity-title {
        width: 13rem;
    }
    .quantity-button-container {
        display: flex;
        border: 1px solid var(--primary-line-color);
        border-radius: 2px;
    }
    .quantity-button-container button {
        padding: 0.6rem 0.8rem;
    }
    .quantity-button-container svg {
        width: 18px;
        height: 18px;
    }
    .quantity-button-container input {
        border: 1px solid var(--primary-line-color);
        text-align: center;
        width: 10rem;
        border: none;
        padding-left: 1rem;
    }
    .quantity-button__plus {
        border: none;
        border-left: 1px solid var(--primary-line-color);
    }
    .quantity-button__minus {
        border: none;
        border-right: 1px solid var(--primary-line-color);
    }
    .order-button-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 2rem
    }
    .order-button-container > button {
        padding: 1rem 0;
        border: 2px solid var(--primary-color);
        border-radius: 3px;
    }
    .order-button--primary {
        background-color: #f0e5f1;
        color: var(--fc-primary-color);
    }
    .order-button--secondary {
        background-color: var(--primary-color);
        color: #fff;
    }
</style>