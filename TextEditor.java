/** Ben Highsted Text Editor Project **/

import java.awt.GraphicsConfiguration;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class TextEditor {

    public static void main(String[] args) {

        JFrame frame = new JFrame();
        frame.setVisible(true);
        frame.setSize(600, 400);
        frame.setTitle("Ben's Text Editor");

        JPanel panel = new JPanel();
        JTextField textWindow = new JTextField(16);
        panel.add(textWindow);

        frame.add(panel);
    }

}