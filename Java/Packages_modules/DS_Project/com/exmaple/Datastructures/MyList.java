package Packages_modules.DS_Project.com.exmaple.Datastructures;

import java.util.ArrayList;

public class MyList {
    private ArrayList<Integer> list = new ArrayList<>();

    public void addElements(int element) {
        list.add(element);
    }

    public void printElements() {
        System.out.print("List: " + list);
    }
}
