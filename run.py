import battle

cpu_board = battle.generateBoard(8,8)
bottom_board = battle.generateBoard(8,8)

battle.populateCPUBoard(cpu_board, 10)


battle.drawBoard(bottom_board)
battle.populatePlayerBoard(bottom_board, 2)
battle.drawBoard(bottom_board)
