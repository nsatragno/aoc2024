Console.WriteLine("Day 01");

string[] input = File.ReadAllLines("input.txt");

int[] left = new int[input.Length];
int[] right = new int[input.Length];

Dictionary<int, int> map = new Dictionary<int, int>();
for (int i = 0; i < input.Length; ++i)
{
    string[] parts = input[i].Split(" ", StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);
    left[i] = int.Parse(parts[0]);
    right[i] = int.Parse(parts[1]);
    if (map.ContainsKey(right[i])) {
        ++map[right[i]];
    } else {
        map[right[i]] = 1;
    }
}

Array.Sort(left);
Array.Sort(right);

int distance = 0;
for (int i = 0; i < left.Length; ++i) {
    distance += Math.Abs(left[i] - right[i]);
}

Console.WriteLine("Distance: " + distance);

int similarity = 0;
foreach (int number in left) {
    if (map.ContainsKey(number)) {
        similarity += number * map[number];
    }
}

Console.WriteLine("Similarity: " + similarity);