import { useRouter } from 'next/router';
import Link from 'next/link';

export default function Payment() {
  const router = useRouter();
  const { show } = router.query;
  return (
    <div>
      <h1>Payment for Show {show}</h1>
      <Link href={`/booking-summary?show=${show}`}>Pay (Mock)</Link>
    </div>
  );
}
