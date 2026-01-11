import Card from './Card';
import { Briefcase, Upload, Cpu, TrendingUp } from 'lucide-react';

const BentoGrid = ({ analysisResult, onUpload }) => {
    const { match_score, extracted_skills, missing_skills, suggested_learning_path } = analysisResult || {};

    return (
        <div className="max-w-7xl mx-auto p-4 grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4 auto-rows-[minmax(180px,auto)]">

            {/* 1. Header / Upload Section (Large) */}
            <Card className="col-span-1 md:col-span-2 lg:col-span-2 row-span-2 flex flex-col justify-center items-center text-center bg-gradient-to-br from-gray-50 to-white">
                <h1 className="text-4xl font-bold text-gray-900 mb-2 font-['Sora']">SkillSync</h1>
                <p className="text-gray-500 mb-6 max-w-sm">Analyze your resume against job descriptions to find your perfect career path.</p>

                <label className="flex flex-col items-center cursor-pointer group">
                    <div className="w-16 h-16 bg-blue-50 text-blue-500 rounded-full flex items-center justify-center mb-2 group-hover:scale-110 transition-transform">
                        <Upload size={28} />
                    </div>
                    <span className="text-sm font-medium text-gray-600">Upload PDF Resume</span>
                    <input type="file" accept=".pdf" className="hidden" onChange={onUpload} />
                </label>
            </Card>

            {/* 2. Match Score (Square) */}
            <Card className="col-span-1 md:col-span-1 row-span-1 flex flex-col items-center justify-center" delay={0.1}>
                <div className="text-gray-400 text-sm mb-1 uppercase tracking-wider font-semibold">Match Score</div>
                <div className={`text-6xl font-bold font-['Sora'] ${match_score > 75 ? 'text-green-500' : match_score > 50 ? 'text-yellow-500' : 'text-gray-300'}`}>
                    {match_score !== undefined ? `${match_score}%` : '--'}
                </div>
            </Card>

            {/* 3. Skills Found (Tall) */}
            <Card className="col-span-1 md:col-span-1 row-span-2 overflow-hidden" delay={0.2}>
                <div className="flex items-center gap-2 mb-4">
                    <Cpu className="text-purple-500" size={20} />
                    <h3 className="font-semibold text-gray-800">Skills Detected</h3>
                </div>
                <div className="flex flex-wrap gap-2">
                    {extracted_skills && extracted_skills.length > 0 ? (
                        extracted_skills.map((skill, idx) => (
                            <span key={idx} className="px-3 py-1 bg-purple-50 text-purple-600 rounded-full text-xs font-medium">
                                {skill}
                            </span>
                        ))
                    ) : (
                        <p className="text-gray-400 text-sm italic">No skills detected yet.</p>
                    )}
                </div>
            </Card>

            {/* 4. Missing Skills (Square) */}
            <Card className="col-span-1 md:col-span-1 row-span-1" delay={0.3}>
                <div className="flex items-center gap-2 mb-2">
                    <Briefcase className="text-red-400" size={20} />
                    <h3 className="font-semibold text-gray-800">Missing</h3>
                </div>
                <div className="flex flex-wrap gap-2">
                    {missing_skills && missing_skills.length > 0 ? (
                        missing_skills.slice(0, 5).map((skill, idx) => (
                            <span key={idx} className="px-2 py-1 border border-red-100 text-red-500 rounded-lg text-xs">
                                {skill}
                            </span>
                        ))
                    ) : (
                        <p className="text-gray-400 text-sm">None</p>
                    )}
                    {missing_skills && missing_skills.length > 5 && <span className="text-xs text-gray-400">+{missing_skills.length - 5} more</span>}
                </div>
            </Card>

            {/* 5. Project Recommendations (New Section) */}
            <Card className="col-span-1 md:col-span-3 lg:col-span-4 row-span-1 bg-gradient-to-r from-blue-50 to-indigo-50" delay={0.4}>
                <div className="flex items-center gap-2 mb-4">
                    <Briefcase className="text-blue-600" size={20} />
                    <h3 className="font-semibold text-gray-800">Recommended Projects to Fill Gaps</h3>
                </div>
                {analysisResult?.project_recommendations && analysisResult.project_recommendations.length > 0 ? (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                        {analysisResult.project_recommendations.map((item, idx) => (
                            <div key={idx} className="bg-white p-4 rounded-xl shadow-sm border border-blue-100">
                                <div className="flex justify-between items-start mb-2">
                                    <span className="text-xs font-bold text-blue-600 bg-blue-50 px-2 py-1 rounded-md uppercase">{item.skill}</span>
                                </div>
                                <p className="text-sm text-gray-600 font-medium leading-relaxed">{item.project}</p>
                            </div>
                        ))}
                    </div>
                ) : (
                    <p className="text-gray-400 text-sm">No missing skills identified or analysis pending.</p>
                )}
            </Card>

            {/* 6. Learning Path (Wide) */}
            <Card className="col-span-1 md:col-span-3 lg:col-span-4 row-span-1" delay={0.5}>
                <div className="flex items-center gap-2 mb-4">
                    <TrendingUp className="text-green-500" size={20} />
                    <h3 className="font-semibold text-gray-800">Recommended Learning Path</h3>
                </div>
                {suggested_learning_path && suggested_learning_path.length > 0 ? (
                    <div className="flex gap-4 overflow-x-auto pb-2">
                        {suggested_learning_path.map((item, idx) => (
                            <div key={idx} className="flex-shrink-0 min-w-[200px] p-4 bg-gray-50 rounded-2xl border border-gray-100">
                                <div className="font-bold text-gray-800 mb-1">{item.skill}</div>
                                <div className="text-xs text-gray-500 mb-2">Prerequisites:</div>
                                <div className="flex flex-wrap gap-1">
                                    {item.prerequisites.map((req, i) => (
                                        <span key={i} className="text-[10px] bg-white border border-gray-200 px-1 py-0.5 rounded text-gray-600">{req}</span>
                                    ))}
                                </div>
                            </div>
                        ))}
                    </div>
                ) : analysisResult ? (
                    missing_skills && missing_skills.length > 0 ? (
                        <div className="p-4 bg-yellow-50 rounded-2xl border border-yellow-100 flex items-center gap-3">
                            <div className="p-2 bg-yellow-100 rounded-full text-yellow-600"><TrendingUp size={18} /></div>
                            <div>
                                <p className="font-bold text-gray-800 text-sm">Self-Paced Learning</p>
                                <p className="text-xs text-gray-600">Your missing skills do not have specific prerequisites in our database. You can start learning them directly!</p>
                            </div>
                        </div>
                    ) : (
                        <div className="p-4 bg-green-50 rounded-2xl border border-green-100 flex items-center gap-3">
                            <div className="p-2 bg-green-100 rounded-full text-green-600"><TrendingUp size={18} /></div>
                            <div>
                                <p className="font-bold text-green-800 text-sm">Ready for Launch! 🚀</p>
                                <p className="text-xs text-green-600">You have all the required skills. Go applied for that job!</p>
                            </div>
                        </div>
                    )
                ) : (
                    <p className="text-gray-400 text-sm">Upload a resume and process it to see your personalized path.</p>
                )}
            </Card>

        </div>
    );
};

export default BentoGrid;
