import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { FarmsPage } from './pages/FarmsPage';
import { FarmsFormPage } from './pages/FarmsFormPage';
import { Navigation } from './components/Navigation';

function App() {
  return (
    <BrowserRouter>
      <Navigation /> 
      <Routes>
        <Route path="/" element={<Navigate to="/farms" />} />
        <Route path="/farms" element={<FarmsPage />} />
        <Route path="/farms/add" element={<FarmsFormPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;