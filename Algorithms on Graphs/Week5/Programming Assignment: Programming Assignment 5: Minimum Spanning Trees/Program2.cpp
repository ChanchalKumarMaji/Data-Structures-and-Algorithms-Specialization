
#include<iostream>
#include<fstream>
#include<bitset> 
#include<vector>
#include<set>
#include<map>
#include<stack> 
#include<queue>
#include<algorithm> 
#include<numeric>
#include<string> 
#include<cstdio> 
#include<cmath>
#include<cstring>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define INF 1000000000

// Common memset settings
//memset(memo, -1, sizeof memo);    // initialize DP memoization table with -1
//memset(arr, 0, sizeof arr);    // to clear array of integers


//-----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "VECTOR" objects 
template<typename T>
ostream& operator << (ostream& o, const vector<T>& v){
    o << "[ ";
    for(int i=0; i<v.size(); i++){
        o << v[i];
        if(i != v.size()-1)
            o << ", ";  
    }     
    o << " ]"; // To include new lines in 2d vectors put " o << " ]\n" " 
    return o;
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "SET" elements 
template<typename T>
ostream& operator << (ostream& o, const set<T>& s){
    o << "[ ";
    for(auto it : s){
        o << it;
        if(it != *s.rbegin())
            o << ", ";
    }
    o << " ]";
    return o;
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "MAP" elements 
template<typename T, typename S>
ostream& operator << (ostream& o, const map<T, S>& m){
    for(auto it : m)
        o << it.first << " : " << it.second << "\n";
    return o;    
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "PAIR" class
template<typename T, typename S>
ostream& operator << (ostream& o, const pair<T, S>& p){
    o << "( ";
    o << p.first << ", " << p.second << " )";
    return o;
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "STACK" objects 
template<typename T>
ostream& operator << (ostream& o, const stack<T>& s){
    o << "[ ";
    stack<T> temp = s;
    while(!temp.empty()){
        o << temp.top();
        temp.pop(); 
        if(temp.size() >= 1)
            o << ", ";  
    }
    o << " ]";
    return o;
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "QUEUE" objects
template<typename T>
ostream& operator << (ostream& o, const queue<T>& q){
    o << "[ ";
    queue<T> temp = q;
    while(!temp.empty()){
        o << temp.front();
        temp.pop(); 
        if(temp.size() >= 1)
            o << ", ";  
    }
    o << " ]";
    return o;
}
//----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "PRIORITY QUEUE" elements 
template<typename T>
ostream& operator << (ostream& o, const priority_queue<T>& q){
    o << "[ ";
    priority_queue<T> temp = q;
    while(!temp.empty()){
        o << temp.top();
        temp.pop(); 
        if(temp.size() >= 1)
            o << ", ";  
    }
    o << " ]";
    return o;
}
//--------------------------------------------------------------------------------------------------------------------------------------------------- 
/*     C++ STL Algorithms 
    1. a. sort(first_iterator, last_iterator) – To sort the given vector
       b. sort(start_iterator, end_iterator, compare_function) - this also sorts the given range but you can define how the sorting should be done by compare_function
    2. reverse(first_iterator, last_iterator) – To reverse a vector
    3. *max_element(first_iterator, last_iterator) – To find the maximum element of a vector 
    4. *min_element(first_iterator, last_iterator) – To find the minimum element of a vector
    5. a. accumulate(first_iterator, last_iterator, initial value of sum) – Does the summation of vector elements
       b. accumulate(first_iterator, last_iterator, initial value of sum, myoperator) 
    6. count(first_iterator, last_iterator, x) – To count the occurrences of x in vector
    7. find(first_iterator, last_iterator, x) – Points to last address of vector ((name_of_vector).end()) if element is not present in vector   
    8. a. binary_search(first_iterator, last_iterator, x) – Tests whether x exists in sorted vector or not
       b. binary_search(first_iterator, last_iterator, value, compare_function)
    9. lower_bound(first_iterator, last_iterator, x) – returns an iterator pointing to the first element in the range [first,last) which has a value not less than x
    10. upper_bound(first_iterator, last_iterator, x) – returns an iterator pointing to the first element in the range [first,last) which has a value greater than x
    11. a. is_sorted(first_iterator, last_iterator) - returns true if the range [first,last) is sorted into ascending order
        b. is_sorted(first_iterator, last_iterator, compare_function) - it also checks the given range but you can define how the sorting must be done
    12. __gcd(m, n) - Handle 0,0 cases separately 
    13.     
*/
//----------------------------------------------------------------------------------------------------------------------------------------------------
// Code for "sort" with user defined way 
struct MyClass{ 
    bool operator () (int i, int j){
        return i>j;
    }
};
MyClass obj;
//----------------------------------------------------------------------------------------------------------------------------------------------------
// Union-Find Disjoint Sets Library written in OOP manner, using both path compression and union by rank heuristics
class UnionFind {                                              // OOP style
private:
  vi p, rank, setSize;                       // remember: vi is vector<int>
  int numSets;
public:
  UnionFind(int N) {
    setSize.assign(N, 1); numSets = N; rank.assign(N, 0);
    p.assign(N, 0); for (int i = 0; i < N; i++) p[i] = i; }
  int findSet(int i) { return (p[i] == i) ? i : (p[i] = findSet(p[i])); }
  bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }
  void unionSet(int i, int j) { 
    if (!isSameSet(i, j)) { numSets--; 
    int x = findSet(i), y = findSet(j);
    // rank is used to keep the tree short
    if (rank[x] > rank[y]) { p[y] = x; setSize[x] += setSize[y]; }
    else                   { p[x] = y; setSize[y] += setSize[x];
                             if (rank[x] == rank[y]) rank[y]++; } } }
  int numDisjointSets() { return numSets; }
  int sizeOfSet(int i) { return setSize[findSet(i)]; }
  vi parent() { return p; }
};
//----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to find "GCD" of two numbers
int gcd(int a, int b){
    if(a==0)
        return b;
    return gcd(b%a, a);    
}
//----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to find the prime numbers using sieve of Erathosthenes 
vector<int> SieveOfErathosthenes(int n){
    vi res;
    vi prime(n+1, 1);
    int p = 2;
    while(p*p <= n){
        if(prime[p]){
            for(int i=2*p; i<n+1; i+=p)
                prime[i] = 0;
        }
        p++;
    }
    for(int i=2; i<n+1; i++){
        if(prime[i])
            res.push_back(i);
    }
    return res;
}
//----------------------------------------------------------------------------------------------------------------------------------------------------
// Code for Fast Modular Exponentiation - Iterative Function to calculate (x^y)%p in O(log y) 
int power(int x, unsigned int y, int p){
    int res = 1;      // Initialize result
    x = x % p;  // Update x if it is more than or 
                // equal to p
    while (y > 0){
        // If y is odd, multiply x with result
        if (y & 1)
            res = (res*x) % p;
        // y must be even now
        y = y>>1; // y = y/2
        x = (x*x) % p;  
    }
    return res;
}
//----------------------------------------------------------------------------------------------------------------------------------------------------
// Code for Graph Algorithms 
vector<vii> AdjList;
vi dfs_num;
int numCC;

void dfs(int u) {          // DFS for normal usage: as graph traversal algorithm
  //printf(" %d", u);                                  // this vertex is visited
  dfs_num[u] = 1;              // important step: we mark this vertex as visited
  for (int j = 0; j < (int)AdjList[u].size(); j++) {
    ii v = AdjList[u][j];                      // v is a (neighbor, weight) pair
    if (dfs_num[v.first] == 0)                 // important check to avoid cycle
      dfs(v.first);      // recursively visits unvisited neighbors v of vertex u
} }
//----------------------------------------------------------------------------------------------------------------------------------------------------
//===================================================================================================================================================
// Your Code starts here

double d(pair<double, double> p1, pair<double, double> p2){ 
    return sqrt(pow((p1.first-p2.first), 2) + pow((p1.second-p2.second), 2)); 
}

int main(){

    int n, k; cin>>n;
    vector<pair<double, double> > points(n); 
    
    double dist[205][205];
    memset(dist, 0, sizeof dist);
    
    for(int i=0; i<n; i++){
        double x, y; cin>>x>>y;
        points[i].first = x;
        points[i].second = y;  
    }
    cin>>k;
    vector<pair<double, ii> > EdgeList;
    for(int i=0; i<n-1; i++)
        for(int j=i+1; j<n; j++){
            double w = d(points[i], points[j]);
            dist[i][j] = w; dist[j][i] = w;
            EdgeList.push_back(make_pair(w, ii(i, j))); 
        }
        
    sort(EdgeList.begin(), EdgeList.end()); 
    
    double mst_cost = 0; 
    vector<double> ans;
    UnionFind UF(n);
    for(int i=0; i<EdgeList.size(); i++){
        pair<double, ii> front = EdgeList[i];
        if (!UF.isSameSet(front.second.first, front.second.second)) {
            mst_cost += front.first;
            UF.unionSet(front.second.first, front.second.second); 
            ans.push_back(dist[front.second.first][front.second.second]); 
        }
    }
    
    printf("%.12f\n", ans[n-k]);                      

return 0;
}
//===================================================================================================================================================

