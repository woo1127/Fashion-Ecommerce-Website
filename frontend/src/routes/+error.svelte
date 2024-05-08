<script>
    import { page } from '$app/stores';
</script>

<div class="error-container">
    <h1>{$page.status}</h1>
    <h2>{$page.error.message}</h2>
</div>


<style>
    .error-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 90vh;
        flex-direction: column;
    }
    h1 {
        font-size: 5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }
    h2 {
        font-size: 2rem;
        font-weight: 500;
    }
</style>