#include <stdio.h>
#include <stdlib.h>
 
#define MAX_TREE_HT 100
 
// �@���N�ҰҾ��I 
struct MinHeapNode {
	char data;         // �r��
	unsigned freq;	   // �r�ťX�{������ 
	struct MinHeapNode *left, *right;
};
 
// �̤p��: �@��ɬ�����C�ϥ�
struct MinHeap {
	unsigned size;     // �̤p�露�����Ӽ� 
	unsigned capacity;  //�̤j�e�q
	struct MinHeapNode **array;
};
 
//��l�Ƥ@�ӳ̤p�ﵲ�I 
struct MinHeapNode* newNode(char data, unsigned freq) {
	struct MinHeapNode* temp = (struct MinHeapNode*) malloc(sizeof(struct MinHeapNode));//�إ߰ʺA�Ȧs(��)
	temp->left = temp->right = NULL;
	temp->data = data;
	temp->freq = freq;
	return temp;
};
 
// �Ыؤ@�Ӯe�q��capacity ���̤p��
struct MinHeap* newMinHeap(unsigned capacity) {
	struct MinHeap* minHeap = (struct MinHeap*)malloc(sizeof(struct MinHeap));
	minHeap->size = 0;
	minHeap->capacity = capacity;
	struct MinHeapNode **array = (struct MinHeapNode **)malloc(minHeap->capacity * sizeof(struct MinHeapNode*));
	minHeap->array = array;
	return minHeap;
};
 
//  swap ��Ӱﵲ�I 
void swapMinHeapNode(struct MinHeapNode **a, struct MinHeapNode **b) {
	struct MinHeapNode* temp = *a;
	*a = *b;
	*b = temp;
}
 
//�o�쥪�Ĥl���I�U�СA�q�{�Ĥ@�Ӹ`�I�U�Ь�0
int getLeftIndex(int index) {
	return ((index << 1) + 1);
}
//�o��k�Ĥl���I�U�СA�q�{�Ĥ@�Ӹ`�I�U�Ь�0
int getRightIndex(int index) {
	return ((index << 1) + 2);
}
// �վ�̤p��
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
//	}   �Ϊ̧A�]�i�H�g���U������ 
	if (less != index) {
		swapMinHeapNode(&minHeap->array[less], &minHeap->array[index]);
		adjustMinHeap(minHeap, less);	
	}
}
 
//�˴��諸�j�p�O�_��1
int isSizeOne(struct MinHeap* minHeap) {
	return (minHeap->size == 1);
}
 
// �˴��O�_�O���l���I 
int isLeaf(struct MinHeapNode* node) {
	return !(node->left) && !(node->right);
}
 
// ���L
void printArr(int arr[], int n)
{
    int i;
    for (i = 0; i < n; ++i)
        printf("%d", arr[i]);
    printf("\n");
}
//���o�襤�̤p�����I 
struct MinHeapNode* extractMin(struct MinHeap* minHeap) {
	struct MinHeapNode* temp = minHeap->array[0];
	minHeap->array[0] = minHeap->array[minHeap->size-1];
	--minHeap->size;
	adjustMinHeap(minHeap, 0);
	return temp;
}
 
// �Q�̤p�襤���J�@�Ӹ`�I 
void insertMinHeap(struct MinHeap* minHeap, struct MinHeapNode* minHeapNode) {
	++minHeap->size;
	int i = minHeap->size - 1;
	while (i && minHeapNode->freq < minHeap->array[(i-1) / 2]->freq) {
		minHeap->array[i] = minHeap->array[(i-1) / 2];
		i = (i-1) / 2;
	}
	minHeap->array[i] = minHeapNode;
}
 
//�۫ؤ@�ӳ̤p��
void buildMinHeap(struct MinHeap* minHeap) {
	int index = minHeap->size - 1;
	int i;
	for (i = (index - 1) / 2; i >= 0; --i) {
		adjustMinHeap(minHeap, i);
	}
}
 
// �Ыؤ@�Ӯe�q�� size���̤p��A�}���J data[] ����������̤p��
struct MinHeap* createAndBuildMinHeap(char data[], int freq[], int size) {
    struct MinHeap* minHeap = newMinHeap(size);
	for (int i = 0; i < size; i++) {
		minHeap->array[i] = newNode(data[i],  freq[i]);
	}
	minHeap ->size = size;
	buildMinHeap(minHeap);
	return minHeap;
}
 
// �۫��N�ҰҾ� 
struct MinHeapNode* buildHuffmanTree(char data[], int freq[], int size) {
	struct MinHeapNode *left, *right, *top;
	// �� 1�B : �Ыس̤p��.
	struct MinHeap* minHeap = createAndBuildMinHeap(data, freq, size);
	//����̤p��u���@�Ӥ���
	while (!isSizeOne(minHeap)) {
		// �ĤG�B: ����̤p����Ӥ���
		left = extractMin(minHeap);
		right = extractMin(minHeap);
		// �ĤT�B: ���u��ӳ̤p�����I�A�ӳЫؤ@�ӷs���������I
        // '$' �u�O�鷺�����I���@�ӯS��аO�A�S���ϥ�
		top = newNode('$', left->freq + right->freq);
		top->left = left;
		top->right = right;
		insertMinHeap(minHeap, top);
	}
	// �ĥ|�B: ���u��ӳ̤p�����I�A�ӳЫؤ@�ӷs���������I
	return extractMin(minHeap);
}
 
// ���L�N�Ұҽs�X
void printCodes(struct MinHeapNode* root, int arr[], int top) {
	if (root->left) {
		arr[top] = 0;
		printCodes(root->left, arr, top + 1);		
	}
	if (root->right) {
		arr[top] = 1;
		printCodes(root->right, arr ,top + 1);
	}
	// �p�G�O���l���I�N���L
	if (isLeaf(root)) {
		printf("%c:", root->data);
		printArr(arr, top);
	} 
}
 
 
// �۫��N�ҰҾ�A�}�M�ߥ��L���N�ҰҾ�
void HuffmanCodes(char data[], int freq[], int size)
{
   //  �۫��N�ҰҾ� 
   struct MinHeapNode* root = buildHuffmanTree(data, freq, size);
   // ���L�۫ئn���N�ҰҾ�
   int arr[MAX_TREE_HT], top = 0;
   printCodes(root, arr, top);
}
 
 
int main() {
	char arr[] = {'a', 'b', 'c', 'd', 'e', 'f'};
    int freq[] = {5, 9, 12, 13, 16, 45};
//	int size = sizeof(arr)/sizeof(char);
	
	//�P�_�x�}���� 
	int size = sizeof(arr)/sizeof(arr[0]);
	printf("size = %d\n",size);
	HuffmanCodes(arr, freq, size);
	return 0;
}
