import { useRouter } from 'next/router';
import Link from 'next/link';

export default function Show() {
  const router = useRouter();
  const { id } = router.query;
  return (
    <div>
      <h1>Show {id}</h1>
      {/* Seat selection grid */}
      <Link href={`/confirm?show=${id}`}>Select Seats</Link>
    </div>
  );
}
