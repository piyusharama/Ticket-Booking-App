import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <h1>Movies</h1>
      <ul>
        {/* Replace with fetched movies */}
        <li><Link href="/movie/1">Sample Movie</Link></li>
      </ul>
    </div>
  );
}
