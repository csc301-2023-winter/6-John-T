import './App.css';
import { Route, Routes } from "react-router-dom";
import MediaPage from './components/MediaPage/MediaPage';
import ScanPage from './components/ScanPage/ScanPage';
import Navbar from './components/Navbar/Navbar';

function App() {
	return (
		<Routes>
			<Route path='/' element={<Navbar />}>
				<Route index element={<ScanPage />} />
				<Route path="/media" element={<MediaPage />} />
			</Route>
		</Routes>
	);
}

export default App;
