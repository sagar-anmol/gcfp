// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://sagar-anmol.github.io',
	base: '/gcfp',
	integrations: [
		starlight({
			title: 'ElderTech Operating System Wiki',
			description: 'The Open Encyclopedia & Master Blueprint for Autonomous Hybrid Eldercare',
			social: [
				{ icon: 'github', label: 'GitHub Repository', href: 'https://github.com/sagar-anmol/gcfp' },
			],
			sidebar: [
				{
					label: '⚡ Executive Overview & Master Blueprint',
					items: [{ autogenerate: { directory: 'overview' } }],
				},
				{
					label: '📚 Clinical Research & Evidence',
					items: [{ autogenerate: { directory: 'clinical' } }],
				},
				{
					label: '🏗️ Platform Architecture & Pillars',
					items: [{ autogenerate: { directory: 'architecture' } }],
				},
				{
					label: '🧭 5 Dynamic Care Tracks',
					items: [{ autogenerate: { directory: 'tracks' } }],
				},
				{
					label: '🛣️ 90-Day Launch Roadmap',
					items: [{ autogenerate: { directory: 'roadmap' } }],
				},
				{
					label: '📈 3-Year Scaling & Unit Economics',
					items: [{ autogenerate: { directory: 'expansion' } }],
				},
				{
					label: '🌐 Market & Competitive Intelligence',
					items: [{ autogenerate: { directory: 'market' } }],
				},
				{
					label: '🔬 Editorial Standards & Research Schema',
					items: [{ autogenerate: { directory: 'guidelines' } }],
				},
			],
		}),
	],
});
