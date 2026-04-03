document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("workoutForm");
    const formSection = document.getElementById("formSection");
    const loadingSection = document.getElementById("loadingSection");
    const resultSection = document.getElementById("resultSection");
    const resetBtn = document.getElementById("resetBtn");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        // Hide form, show loading
        formSection.classList.add("hidden");
        loadingSection.classList.remove("hidden");

        // Parse inputs
        const targetMuscleInput = document.getElementById("targetMuscle").value;
        const payload = {
            user_info: {
                age: parseInt(document.getElementById("age").value),
                gender: document.getElementById("gender").value
            },
            goals: {
                current_weight_kg: parseFloat(document.getElementById("currentWeight").value),
                target_weight_kg: parseFloat(document.getElementById("targetWeight").value),
                target_muscle_mass_kg: targetMuscleInput ? parseFloat(targetMuscleInput) : null,
                primary_goal: document.getElementById("primaryGoal").value
            }
        };

        try {
            // Hit FastAPI Recommendation Endpoint
            const response = await fetch("/api/v1/recommend", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error("Failed to fetch recommendation");
            }

            const data = await response.json();
            
            // Populate Results
            populateResults(data);

            // Hide loading, show results
            loadingSection.classList.add("hidden");
            resultSection.classList.remove("hidden");

        } catch (error) {
            console.error(error);
            alert("Error communicating with the API Server.");
            loadingSection.classList.add("hidden");
            formSection.classList.remove("hidden");
        }
    });

    resetBtn.addEventListener("click", () => {
        resultSection.classList.add("hidden");
        form.reset();
        formSection.classList.remove("hidden");
    });

    function populateResults(data) {
        document.getElementById("resProgramName").textContent = data.program_name;
        document.getElementById("resDifficulty").textContent = data.difficulty_level;
        document.getElementById("resDuration").textContent = data.estimated_duration_minutes;

        const EX_CONTAINER = document.getElementById("resExercises");
        EX_CONTAINER.innerHTML = ""; // clear previous

        data.exercises.forEach(ex => {
            const card = document.createElement("div");
            card.className = "exercise-card";

            card.innerHTML = `
                <div>
                    <div class="ex-name">${ex.name}</div>
                    <div class="ex-details">
                        <span>${ex.sets} Sets</span>
                        <span>•</span>
                        <span>${ex.reps} Reps</span>
                    </div>
                </div>
                <div class="ex-rest">Rest: ${ex.rest_seconds}s</div>
            `;
            EX_CONTAINER.appendChild(card);
        });
    }
});
