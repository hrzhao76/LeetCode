#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> return_ints;
        for(int i=0; i<nums.size()-1; i++){
            for(int j=i+1; j<nums.size(); j++){
                if (nums[i] + nums[j] == target){
                    return_ints.push_back(i);
                    return_ints.push_back(j);
                }
            }
        }

        return return_ints;
    }
};