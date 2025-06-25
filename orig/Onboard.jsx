import React from "react";

export default function AfterWordsOnboarding() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-indigo-50 to-white flex flex-col items-center py-12 px-4">
      <div className="w-full max-w-2xl bg-white rounded-2xl shadow-xl p-8">
        <h1 className="text-4xl font-bold text-indigo-800 mb-2">Welcome to AfterWords</h1>
        <h2 className="text-xl font-semibold text-indigo-600 mb-6 italic">
          Leave a Legacy That Will Last Forever
        </h2>

        <section className="mb-8">
          <p className="text-lg mb-2">Your journey starts here. Let’s build your digital legacy together.</p>
          <ol className="list-decimal ml-5 space-y-3 mt-4 text-base">
            <li>
              <span className="font-semibold text-indigo-700">Upload Your Stories</span> <br />
              <span className="text-gray-700">
                Letters, memoirs, emails, stories, advice columns—even journals. <br />
                <span className="italic">Minimum: 5,000 words (about 10 pages)<br />Recommended: 50,000+ words</span>
              </span>
            </li>
            <li>
              <span className="font-semibold text-indigo-700">Add Your Voice <span className="text-xs font-normal text-gray-500">(Optional)</span></span><br />
              <span className="text-gray-700">
                Record or upload 5–30 minutes of clear audio. Read stories, answer questions, or just talk about your life.
              </span>
            </li>
            <li>
              <span className="font-semibold text-indigo-700">Review and Personalize</span><br />
              <span className="text-gray-700">
                See your progress, add a short bio or favorite quote, and preview your avatar.
              </span>
            </li>
            <li>
              <span className="font-semibold text-indigo-700">Privacy and Legacy Settings</span><br />
              <span className="text-gray-700">
                Choose who can interact: Only you, Family & friends, or Public. Decide when to unlock your avatar.
              </span>
            </li>
          </ol>
        </section>

        <section className="mb-8">
          <h3 className="text-lg font-semibold mb-2 text-indigo-800">Onboarding Checklist</h3>
          <ul className="list-disc ml-6 text-base text-gray-700 space-y-2">
            <li>Upload at least <span className="font-medium">5,000 words</span> of your personal writing</li>
            <li>(Optional) Upload at least <span className="font-medium">5 minutes</span> of your voice</li>
            <li>Complete your profile <span className="text-sm text-gray-500">(name, short bio)</span></li>
            <li>Set your privacy and legacy preferences</li>
          </ul>
          <div className="bg-indigo-100 rounded-lg mt-4 p-3 text-sm text-indigo-700">
            <span className="font-semibold">Tip:</span> The more you share, the richer and more lifelike your AfterWords avatar will be!
          </div>
        </section>

        <section className="mb-8">
          <h3 className="text-lg font-semibold mb-2 text-indigo-800">What to Expect</h3>
          <ul className="text-base text-gray-700 list-disc ml-6 space-y-1">
            <li>Your avatar only knows what you share—add stories, advice, memories for the best results.</li>
            <li>You can add more content anytime—your legacy grows as you do.</li>
            <li>Your data is private and secure. You control everything.</li>
          </ul>
        </section>

        <div className="flex justify-center">
          <button className="bg-indigo-700 hover:bg-indigo-800 text-white font-semibold py-3 px-8 rounded-2xl shadow transition text-lg">
            Get Started
          </button>
        </div>
      </div>
    </div>
  );
}
