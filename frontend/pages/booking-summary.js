import { useRouter } from 'next/router';

export default function BookingSummary() {
  const router = useRouter();
  const { show } = router.query;
  return (
    <div>
      <h1>Booking Summary for Show {show}</h1>
      <p>Your booking is confirmed!</p>
    </div>
  );
}
