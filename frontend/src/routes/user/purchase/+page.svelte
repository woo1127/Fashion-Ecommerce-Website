<script>
    /** @type {import('./$types').PageData} */
    export let data
    let { orders }  = data
</script>

<svelte:head>
    <title>Purchase History | LUXE Malaysia</title>
</svelte:head>

<div class="page-content">
    <div class="container">
        <div class="title"></div>
        {#each orders as order}
            <div class="order-container">
                <div class="order-header">
                    <span>Order ID</span>
                    <h3>{order.id}</h3>
                </div>
                <div class="order-content">
                    {#each order.items as item}
                        <div class="order-item">
                            <div class="order-image">
                                <picture>
                                    <img src="{item.color_detail.url}" alt="" loading="lazy">
                                </picture>
                            </div>
                            <div class="order-info">
                                <h3 class="order-name">{item.product_detail.name}</h3>
                                <div class="order-field">
                                    <p class="order-field__title">Color:</p>
                                    {#if item.color_detail.secondary_color}
                                        <p class="order-field__value">{item.color_detail.primary_color} / {item.color_detail.secondary_color}</p>
                                    {:else}
                                        <p class="order-field__value">{item.color_detail.primary_color}</p>
                                    {/if}
                                </div>
                                <div class="order-field">
                                    <p class="order-field__title">Size:</p>
                                    <p class="order-field__value">{item.size_detail.value}</p>
                                </div>
                                <div class="order-field">
                                    <p class="order-field__title">Quantity:</p>
                                    <p class="order-field__value">{item.quantity}</p>
                                </div>
                            </div>  
                            <div class="order-price">
                                S$ {item.total_price}
                            </div>
                        </div>
                    {/each}
                </div>
                <div class="order-footer">
                    <div class="order-footer__price">
                        <span>Total</span>
                        <span>S$ {order.total_price}</span>
                    </div>
                    <!-- <button id="buy-again-btn">Buy Again</button> -->
                </div>
            </div>
        {/each}
    </div>
</div>

<style>
    .container {
        padding: 4rem 15%;
    }
    .title {
        padding: 0 1rem 2.5rem 1rem;
        font-size: 2.5rem;
        font-weight: 700;
    }
    .order-container {
        background-color: #fff;
        box-shadow: 0 1px 1px 0 rgba(0, 0, 0, .05);
        border-radius: 3px;
        margin-bottom: 3rem;
    }
    .order-header {
        padding: 2rem 3.5rem;
        border-bottom: 1px solid var(--primary-line-color);
    }
    .order-header h3 {
        font-size: 2.1rem;
        font-weight: 600;
    }
    .order-header span {
        display: block;
        font-size: 1.2rem;
        padding-bottom: 0.5rem;
    }
    .order-content {
        padding: 2rem 2.5rem;
        border-bottom: 1px solid var(--primary-line-color);
    }
    .order-item {
        display: flex;
        justify-content: space-between;       
        align-items: center; 
        padding: 1.2rem 0;
        border-bottom: 1px solid var(--primary-line-color);
    }
    .order-item:first-child {
        padding-top: 0;
    }
    .order-item:last-child {
        border: none;
        padding-bottom: 0;
    }
    .order-image {
        width: 120px;
        height: auto;
        aspect-ratio: 1/1;
    }
    .order-info {
        padding-left: 2rem;
        flex: 1;
    }
    .order-info > * {
        margin-bottom: 1rem;
    }
    .order-name {
        font-size: 1.6rem;
        font-weight: 500;
    }
    .order-field {
        width: 50%;
        display: flex;
        gap: 1.5rem;
        align-items: center;
    }
    .order-field__title {
        text-align: left;
    }
    .order-field__value {
        text-align: right;
    }
    .order-price {
        font-size: 1.6rem;   
    }
    .order-footer {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        padding: 3rem 3rem;
    }
    .order-footer__price {
        display: flex;
        align-items: center;
        gap: 2rem;
        text-align: right;
        /* padding-bottom: 2rem; */
    }
    .order-footer__price > span:first-child{
        font-size: 1.6rem;
        font-weight: 500;
    }
    .order-footer__price > span:nth-child(2){
        font-size: 2.1rem;
        font-weight: 600;
        
    }
    .order-footer #buy-again-btn {
        padding: 1rem 3rem;
        background-color: var(--primary-color);
        color: #fff;
        border: none;
        border-radius: 3px;
        font-size: 1.6rem;
    }
</style>
