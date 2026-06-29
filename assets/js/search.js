export function scoreItem(item, query){const q=query.toLowerCase();return JSON.stringify(item).toLowerCase().includes(q)?1:0;}
