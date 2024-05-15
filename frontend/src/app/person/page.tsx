import { z } from 'zod';

const Person = z.object({
    id: z.string().min(32).max(32),
    created_at: z.string().datetime(),
    updated_at: z.string().datetime(),
    name: z.string().min(1),
    surname: z.string().min(1),
    patronymic: z.string().min(1),
    gender: z.enum(['male', 'female']),
    birth_date: z.string().date(),
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
                    <p>{person.name}</p>
                    <p>{person.surname}</p>
                    <p>{person.patronymic}</p>
                    <p>{person.birth_date}</p>
                    <p>{person.gender}</p>
                </>
            ))}
        </>
    );
}
