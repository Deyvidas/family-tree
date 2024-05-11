import { z } from 'zod';

const Person = z.object({
    id: z.string(),
    created_at: z.string().datetime(),
    updated_at: z.string().datetime().nullable(),
    first_name: z.string(),
    last_name: z.string(),
});

const People = z.array(Person);

type People = z.infer<typeof People>;

async function getPersons(): Promise<People> {
    const url = 'http://localhost:8000/api/v1/person';
    const res = await fetch(url, { next: { revalidate: 60 * 5 } });

    if (!res.ok) {
        throw new Error(`Failed to fetch data on ${url}`);
    }

    return People.parse(await res.json());
}

export default async function AllPage() {
    const persons = await getPersons();

    return (
        <>
            {persons.map(person => (
                <>
                    <p>{person.id}</p>
                    <p>{person.created_at}</p>
                    <p>{person.updated_at}</p>
                    <p>{person.first_name}</p>
                    <p>{person.last_name}</p>
                </>
            ))}
        </>
    );
}
