Here's the information from the image turned into a Markdown table:

**WHY ROTATE CASE**

| Case           | Description                                                                                             | Rotation to Restore Balance                                                                                             |
| :------------- | :------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------- |
| Left-Left (LL) | The unbalanced node and its left child node are both left-heavy.                                        | A single right rotation.                                                                                                |
| Right-Right (RR) | The unbalanced node and its right child node are both right-heavy.                                      | A single left rotation.                                                                                                 |
| Left-Right (LR) | The unbalanced node is left heavy, and its left child node is right heavy.                              | First do a left rotation on the left child node, then do a right rotation on the unbalanced node.                       |
| Right-Left (RL) | The unbalanced node is right heavy, and its right child node is left heavy.                             | First do a right rotation on the right child node, then do a left rotation on the unbalanced node.                      |



