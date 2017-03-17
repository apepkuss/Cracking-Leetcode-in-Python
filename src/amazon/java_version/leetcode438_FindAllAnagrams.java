

public class Solution {
    public List<Integer> findAnagrams_ASCIITable(String s, String p) {

        List<Integer> res = new ArrayList<>();

        if (s == null || s.length() == 0 || p == null || p.length() == 0 || s.length() < p.length()) {
            return res;
        }

        // create a ASCII table
        int[] table = new int[256];
        for (char c : p.toCharArray()) {
            table[c] += 1;
        }

        int left = 0, right = 0;
        int count = p.length();
        while (right < s.length()) {

            // check right
            if (table[s.charAt(right)] >= 1) {
                count -= 1;
            }
            // update table
            table[s.charAt(right)] -= 1;
            // move right
            right += 1;

            if (count == 0) {
                res.add(left);
            }

            // check and move left
            if (right - left == p.length()) {
                // recover the number
                if (table[s.charAt(left)] >= 0) {
                    count += 1;
                }
                // recover table
                table[s.charAt(left)] += 1;
                // move left
                left += 1;
            }
        }

        return res;
    }

    public List<Integer> findAnagrams_HashTable(String s, String p) {

        List<Integer> res = new ArrayList<>();

        if (s == null || s.length() == 0 || p == null || p.length() == 0 || s.length() < p.length()) {
            return res;
        }

        // create a hash table
        Map<Character, Integer> map = new HashMap<>();
        for (char c : p.toCharArray()) {
            if (map.containsKey(c)) {
                map.put(c, map.get(c)+1);
            } else {
                map.put(c, 1);
            }
        }

        int match = 0;
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                map.put(c, map.get(c)-1);
                if (map.get(c) == 0) {
                    match += 1;
                }
            }

            if (i >= p.length()) {
                c = s.charAt(i - p.length());
                if (map.containsKey(c)) {
                    map.put(c, map.get(c)+1);
                    if (map.get(c) == 1) {
                        match -= 1;
                    }
                }
            }

            if (match == map.size()) {
                res.add(i - p.length() + 1);
            }
        }

        return res;
    }
}