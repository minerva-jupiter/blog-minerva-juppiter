import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

// Function to get the D1 database instance
const getDatabase = (platform: { env: { DB: any } }) => {
    if (!platform?.env?.DB) {
        throw new Error('D1 database is not configured.');
    }
    return platform.env.DB;
};

export const load: PageServerLoad = async ({ params, platform }) => {
    if (!platform) {
        throw error(500, 'Platform is not defined.');
    }
    const post = await getPostFromDatabase(platform, params.ArticleNumber);

    if (post) {
        return post;
    }

    throw error(404, 'Not found');
};

const getPostFromDatabase = async (
    platform: { env: { DB: any } },
    slug: string
): Promise<{ title: string; content: string } | null> => {
    const db = getDatabase(platform);

    const query = 'SELECT title, content FROM posts WHERE slug = ?';
    const result = await db.prepare(query).bind(slug).first();

    if (result) {
        return { title: result.title, content: result.content };
    }

    return null;
};