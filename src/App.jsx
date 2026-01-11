import { useState } from 'react';
import BentoGrid from './components/BentoGrid';
import { motion, AnimatePresence } from 'framer-motion';
import { Loader2 } from 'lucide-react';

function App() {
  const [analysisResult, setAnalysisResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Default JD text
  const [jobDescription, setJobDescription] = useState("We are looking for a Data Scientist with experience in Python, Machine Learning, Deep Learning, SQL, and Statistics. Skills in NLP and MLOps are a plus. Experience with Docker is required.");

  const handleUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription); // Send raw text

    const apiUrl = import.meta.env.VITE_API_URL || "http://localhost:8000";

    try {
      const response = await fetch(`${apiUrl}/analyze`, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Analysis failed");
      }

      const data = await response.json();
      setAnalysisResult(data);
    } catch (err) {
      console.error(err);
      setError("Failed to analyze resume. Please ensure backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#F8F9FA] p-8 font-sans text-gray-900">
      <div className="max-w-7xl mx-auto mb-8 flex flex-col md:flex-row justify-between items-start gap-4">
        <div>
          <h2 className="text-xl font-bold font-['Sora'] text-gray-800">Job Description Analysis</h2>
          <p className="text-sm text-gray-500">Paste the full Job Description here. AI will extract the required skills.</p>
        </div>
        <div className="w-full md:w-2/3">
          <label className="text-xs font-semibold uppercase text-gray-400 mb-1 block">Job Description</label>
          <textarea
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            className="w-full p-4 rounded-xl border border-gray-200 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-100 font-medium text-gray-700 min-h-[120px]"
            placeholder="Paste Job Description here..."
          />
        </div>
      </div>

      <AnimatePresence mode="wait">
        {loading ? (
          <motion.div
            key="loader"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="flex flex-col items-center justify-center min-h-[400px]"
          >
            <Loader2 className="animate-spin text-blue-500 mb-4" size={48} />
            <p className="text-gray-500 font-medium animate-pulse">Analyzing Resume & Mapping Career Path...</p>
          </motion.div>
        ) : (
          <motion.div
            key="content"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          >
            {error && (
              <div className="text-center p-4 bg-red-50 text-red-500 rounded-xl mb-8 border border-red-100 max-w-lg mx-auto">
                {error}
              </div>
            )}
            <BentoGrid analysisResult={analysisResult} onUpload={handleUpload} />
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

export default App;
