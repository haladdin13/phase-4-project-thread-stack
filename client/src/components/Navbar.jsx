export default function Navbar(){
    return <nav className="nav">
        <a href='/' className="site-title">Thread Stack</a>
        <ul>
            <li>
                <a href="/dashboard">Dashboard</a>
            </li>
            <li>
                <a href="/categories">Categories</a>
            </li>
            <li>
                <a href="/user">User</a>
            </li>
        </ul>
    </nav>
}