public class BubbleSort {
    /**
     * 冒泡排序算法
     * 时间复杂度: O(n²)
     * 空间复杂度: O(1)
     * 
     * @param arr 待排序的数组
     */
    public static void bubbleSort(int[] arr) {
        if (arr == null || arr.length == 0) {
            return;
        }
        
        int n = arr.length;
        
        // 外层循环：需要进行 n-1 次比较
        for (int i = 0; i < n - 1; i++) {
            // 标志位：用于优化，如果某次遍历没有交换，说明已排序
            boolean swapped = false;
            
            // 内层循环：每次比较相邻元素
            for (int j = 0; j < n - 1 - i; j++) {
                // 如果左边元素大于右边元素，交换
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            
            // 如果没有交换，说明数组已排序，提前退出
            if (!swapped) {
                break;
            }
        }
    }
    
    /**
     * 冒泡排序 - 降序排列
     * 
     * @param arr 待排序的数组
     */
    public static void bubbleSortDescending(int[] arr) {
        if (arr == null || arr.length == 0) {
            return;
        }
        
        int n = arr.length;
        
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            
            for (int j = 0; j < n - 1 - i; j++) {
                // 如果左边元素小于右边元素，交换（降序）
                if (arr[j] < arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            
            if (!swapped) {
                break;
            }
        }
    }
    
    /**
     * 打印数组
     * 
     * @param arr 要打印的数组
     */
    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        // 测试用例 1：普通数组
        int[] arr1 = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("原数组：");
        printArray(arr1);
        
        bubbleSort(arr1);
        System.out.println("升序排列后：");
        printArray(arr1);
        
        // 测试用例 2：降序排列
        int[] arr2 = {64, 34, 25, 12, 22, 11, 90};
        bubbleSortDescending(arr2);
        System.out.println("降序排列后：");
        printArray(arr2);
        
        // 测试用例 3：已排序数组（优化效果）
        int[] arr3 = {1, 2, 3, 4, 5};
        System.out.println("已排序数组：");
        printArray(arr3);
        bubbleSort(arr3);
        System.out.println("排序后：");
        printArray(arr3);
        
        // 测试用例 4：单个元素
        int[] arr4 = {42};
        bubbleSort(arr4);
        System.out.println("单元素数组排序后：");
        printArray(arr4);
    }
}