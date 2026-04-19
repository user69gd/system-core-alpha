#include <iostream>
#include <vector>
#include <numeric>

class HardwareLogic {
public:
    // Simulates a high-speed calculation that would be slower in Python
    double process_signal(const std::vector<int>& signals) {
        if (signals.empty()) return 0.0;

        double sum = std::accumulate(signals.begin(), signals.end(), 0.0);
        return sum / signals.size(); // Returns the average signal strength
    }
};

int main() {
    HardwareLogic logic;
    std::vector<int> data = {102, 405, 303, 908, 112};

    std::cout << "--- C++ Hardware Logic Core ---" << std::endl;
    std::cout << "Processing " << data.size() << "data packets..." << std::endl;

    double result = logic.process_signal(data);

    std::cout << "Calculation Complete. Mean Signal: " << result << std::endl;

    return 0;
}
