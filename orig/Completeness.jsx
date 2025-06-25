// completeness = number (0-100) calculated from user progress

<div className="mb-6">
  <label className="block font-semibold text-gray-700 mb-2">Onboarding Progress</label>
  <div className="w-full bg-gray-200 rounded-full h-6 mb-2">
    <div
      className="bg-indigo-600 h-6 rounded-full transition-all duration-300"
      style={{ width: `${completeness}%` }}
    ></div>
  </div>
  <p className="text-indigo-700 font-semibold">
    {completeness}% complete {completeness < 100 && "- Add more to unlock all features!"}
  </p>
</div>
