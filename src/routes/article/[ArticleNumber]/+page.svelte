<script lang="ts">
    import type { PageProps } from './$types';
    import articles from '$lib/assets/articles.json';

    let { data }: PageProps = $props();
</script>

<h1>{articles[data.content].ArticleName}</h1>

<h4>{articles[data.content].Date}</h4>

<p>{articles[data.content].ArticleBody}</p>

<style>
    h1{
        padding: 4rem;
    }
    h4 {
        padding: 4rem;
    }
    p {
        padding: 4rem;
    }
</style>