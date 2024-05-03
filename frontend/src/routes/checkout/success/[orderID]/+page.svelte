<script>
    /** @type {import('./$types').PageData} */
    export let data
    let { order } = data
</script>

<svelte:head>
    <title>Checkout Sucess | LUXE Malaysia</title>
</svelte:head>

<div class="page-content">
    <div class="container">
        <div class="header">
            <div class="header__icon">
                <svg fill="#54cc77" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52" enable-background="new 0 0 52 52" xml:space="preserve" stroke="#54cc77"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M26,2C12.7,2,2,12.7,2,26s10.7,24,24,24s24-10.7,24-24S39.3,2,26,2z M39.4,20L24.1,35.5 c-0.6,0.6-1.6,0.6-2.2,0L13.5,27c-0.6-0.6-0.6-1.6,0-2.2l2.2-2.2c0.6-0.6,1.6-0.6,2.2,0l4.4,4.5c0.4,0.4,1.1,0.4,1.5,0L35,15.5 c0.6-0.6,1.6-0.6,2.2,0l2.2,2.2C40.1,18.3,40.1,19.3,39.4,20z"></path> </g></svg>
            </div>
            <h1 class="header__title">Payment Sucessfully</h1>
            <p class="header__text">Congratulations! Your exquisite taste shines through once again. Thank you for choosing LUXE to elevate your style journey</p>
        </div>
        <div class="detail">
            <div class="detail-item">
                <p class="detail-item__title">Pay By</p>
                <p class="detail-item__value">{order.username}</p>
            </div>
            <div class="detail-item">
                <p class="detail-item__title">Payment Method</p>
                <p class="detail-item__value">{order.payment_method}</p>
            </div>
            <div class="detail-item">
                <p class="detail-item__title">Amount Paid</p>
                <p class="detail-item__value">S$ {order.total_price}</p>
            </div>
            <div class="detail-item">
                <p class="detail-item__title">Transaction ID</p>
                <p class="detail-item__value">{order.transaction_id}</p>
            </div>
            <div class="detail-item">
                <p class="detail-item__title">Completed Time</p>
                <p class="detail-item__value">{order.created_at}</p>
            </div>
        </div>
        <button class="btn">
            <a href="/">Back to Home</a>
        </button>
    </div>
</div>

<style>
    .container {
        width: 50vw;
        display: flex;
        flex-direction: column;
        margin: 3rem auto;
        margin-top: calc(10vh + 3rem);
        padding: 3rem;
        background-color: #fff;
        border-radius: 3px;
        box-shadow: 0 1px 1px 0 rgba(0, 0, 0, .05);
    }
    .header {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .header > * {
        margin-bottom: 1.5rem;
    }
    .header__icon {
        width: 96px;
        height: 96px;
        aspect-ratio: 1/1;
    }
    .header__title {
        font-size: 1.6rem;
    }
    .header__text,
    .header__title {
        text-align: center;
    }
    .detail {
        padding: 3rem 0;
    }
    .detail-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        border-bottom: 1px solid var(--primary-line-color);
    }
    .detail-item__title {
        text-align: left;
    }
    .detail-item__value {
        font-size: 1.5rem;
        text-align: right;
    }
    .btn {
        align-self: center;
        background-color: var(--primary-color);
        color: #fff;
        padding: 0.8rem 2.4rem;
        border: none;
        border-radius: 3px;
    }
</style>