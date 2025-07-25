import { useRouter } from 'next/router';
import Link from 'next/link';

export default function Movie() {
  const router = useRouter();
  const { id } = router.query;
  return (
    <div>
      <h1>Movie {id}</h1>
      {/* Show details and list of shows */}
      <Link href={`/show/1`}>Go to Show</Link>
    </div>
  );
}
