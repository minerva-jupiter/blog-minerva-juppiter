import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
	const post = await getPostFromDatabase(params.ArticleNumber);

	if (post) {
		return post;
	}

	error(404, 'Not found');
};

const getPostFromDatabase = (slug: string): { title: string; content: number } => {
	// Replace the following with actual database fetching logic
    let article_number = Number(slug);
	return { title: slug, content: article_number };
};