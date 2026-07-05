class Solution:
    def longestMountain(self, arr: List[int]):

        n = len(arr)
        ans = 0
        i = 1

        while i < n - 1:

            # Check if current element is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:

                left = i
                right = i

                # Expand to the left
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                # Expand to the right
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                ans = max(ans, right - left + 1)

                # Skip this mountain
                i = right

            else:
                i += 1

        return ans