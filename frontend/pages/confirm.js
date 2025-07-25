import { useRouter } from 'next/router';
import Link from 'next/link';

export default function Confirm() {
  const router = useRouter();
  const { show } = router.query;
  return (
    <div>
      <h1>Confirm Seats for Show {show}</h1>
      <Link href={`/payment?show=${show}`}>Proceed to Payment</Link>
    </div>
  );
}
