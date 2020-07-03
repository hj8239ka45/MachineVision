#include <stdio.h>
#include <stdlib.h>
 
#define MAX_TREE_HT 100
 
// 一個霍夫曼樹結點 
struct MinHeapNode {
	char data;         // 字符
	unsigned freq;	   // 字符出現的次數 
	struct MinHeapNode *left, *right;
};
 
// 最小堆: 作為优先隊列使用
struct MinHeap {
	unsigned size;     // 最小堆元素的個數 
	unsigned capacity;  //最大容量
	struct MinHeapNode **array;
};
 
//初始化一個最小堆結點 
struct MinHeapNode* newNode(char data, unsigned freq) {
	struct MinHeapNode* temp = (struct MinHeapNode*) malloc(sizeof(struct MinHeapNode));//建立動態暫存(堆)
	temp->left = temp->right = NULL;
	temp->data = data;
	temp->freq = freq;
	return temp;
};
 
// 創建一個容量為capacity 的最小堆
struct MinHeap* newMinHeap(unsigned capacity) {
	struct MinHeap* minHeap = (struct MinHeap*)malloc(sizeof(struct MinHeap));
	minHeap->size = 0;
	minHeap->capacity = capacity;
	struct MinHeapNode **array = (struct MinHeapNode **)malloc(minHeap->capacity * sizeof(struct MinHeapNode*));
	minHeap->array = array;
	return minHeap;
};
 
//  swap 兩個堆結點 
void swapMinHeapNode(struct MinHeapNode **a, struct MinHeapNode **b) {
	struct MinHeapNode* temp = *a;
	*a = *b;
	*b = temp;
}
 
//得到左孩子結點下標，默認第一個節點下標為0
int getLeftIndex(int index) {
	return ((index << 1) + 1);
}
//得到右孩子結點下標，默認第一個節點下標為0
int getRightIndex(int index) {
	return ((index << 1) + 2);
}
// 調整最小堆
void adjustMinHeap(struct MinHeap* minHeap, int index) {
	int less = index;
	int left = getLeftIndex(index);
	int right = getRightIndex(index);
	if (left < minHeap->size && minHeap->array[left]->freq < minHeap->array[less]->freq) {
		less = left;
	}
	if (right < minHeap->size && minHeap->array[right]->freq < minHeap->array[less]->freq) {
		less = right;
	}
//	if (less = index) {
//		return;
//	} else {
//		swapMinHeapNode(&minHeap->array[less], &minHeap->array[index]);
//		adjustMinHeap(minHeap, less);
//	}   或者你也可以寫成下面那樣 
	if (less != index) {
		swapMinHeapNode(&minHeap->array[less], &minHeap->array[index]);
		adjustMinHeap(minHeap, less);	
	}
}
 
//檢測堆的大小是否為1
int isSizeOne(struct MinHeap* minHeap) {
	return (minHeap->size == 1);
}
 
// 檢測是否是葉子結點 
int isLeaf(struct MinHeapNode* node) {
	return !(node->left) && !(node->right);
}
 
// 打印
void printArr(int arr[], int n)
{
    int i;
    for (i = 0; i < n; ++i)
        printf("%d", arr[i]);
    printf("\n");
}
//取得堆中最小的結點 
struct MinHeapNode* extractMin(struct MinHeap* minHeap) {
	struct MinHeapNode* temp = minHeap->array[0];
	minHeap->array[0] = minHeap->array[minHeap->size-1];
	--minHeap->size;
	adjustMinHeap(minHeap, 0);
	return temp;
}
 
// 想最小堆中插入一個節點 
void insertMinHeap(struct MinHeap* minHeap, struct MinHeapNode* minHeapNode) {
	++minHeap->size;
	int i = minHeap->size - 1;
	while (i && minHeapNode->freq < minHeap->array[(i-1) / 2]->freq) {
		minHeap->array[i] = minHeap->array[(i-1) / 2];
		i = (i-1) / 2;
	}
	minHeap->array[i] = minHeapNode;
}
 
//构建一個最小堆
void buildMinHeap(struct MinHeap* minHeap) {
	int index = minHeap->size - 1;
	int i;
	for (i = (index - 1) / 2; i >= 0; --i) {
		adjustMinHeap(minHeap, i);
	}
}
 
// 創建一個容量為 size的最小堆，并插入 data[] 中的元素到最小堆
struct MinHeap* createAndBuildMinHeap(char data[], int freq[], int size) {
    struct MinHeap* minHeap = newMinHeap(size);
	for (int i = 0; i < size; i++) {
		minHeap->array[i] = newNode(data[i],  freq[i]);
	}
	minHeap ->size = size;
	buildMinHeap(minHeap);
	return minHeap;
}
 
// 构建霍夫曼樹 
struct MinHeapNode* buildHuffmanTree(char data[], int freq[], int size) {
	struct MinHeapNode *left, *right, *top;
	// 第 1步 : 創建最小堆.
	struct MinHeap* minHeap = createAndBuildMinHeap(data, freq, size);
	//直到最小堆只有一個元素
	while (!isSizeOne(minHeap)) {
		// 第二步: 取到最小的兩個元素
		left = extractMin(minHeap);
		right = extractMin(minHeap);
		// 第三步: 根据兩個最小的結點，來創建一個新的內部結點
        // '$' 只是對內部結點的一個特殊標記，沒有使用
		top = newNode('$', left->freq + right->freq);
		top->left = left;
		top->right = right;
		insertMinHeap(minHeap, top);
	}
	// 第四步: 根据兩個最小的結點，來創建一個新的內部結點
	return extractMin(minHeap);
}
 
// 打印霍夫曼編碼
void printCodes(struct MinHeapNode* root, int arr[], int top) {
	if (root->left) {
		arr[top] = 0;
		printCodes(root->left, arr, top + 1);		
	}
	if (root->right) {
		arr[top] = 1;
		printCodes(root->right, arr ,top + 1);
	}
	// 如果是葉子結點就打印
	if (isLeaf(root)) {
		printf("%c:", root->data);
		printArr(arr, top);
	} 
}
 
 
// 构建霍夫曼樹，并遍立打印該霍夫曼樹
void HuffmanCodes(char data[], int freq[], int size)
{
   //  构建霍夫曼樹 
   struct MinHeapNode* root = buildHuffmanTree(data, freq, size);
   // 打印构建好的霍夫曼樹
   int arr[MAX_TREE_HT], top = 0;
   printCodes(root, arr, top);
}
 
 
int main() {
	char arr[] = {'a', 'b', 'c', 'd', 'e', 'f'};
    int freq[] = {5, 9, 12, 13, 16, 45};
//	int size = sizeof(arr)/sizeof(char);
	
	//判斷矩陣長度 
	int size = sizeof(arr)/sizeof(arr[0]);
	printf("size = %d\n",size);
	HuffmanCodes(arr, freq, size);
	return 0;
}
