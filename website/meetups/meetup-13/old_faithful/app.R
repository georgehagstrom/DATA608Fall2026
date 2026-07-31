#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    https://shiny.posit.co/
#

library(shiny)
library(tidyverse)
library(ggplot2)
library(ggthemes)
# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("Old Faithful Geyser Data"),

    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            sliderInput("bins",
                        "Number of bins:",
                        min = 1,
                        max = 50,
                        value = 30)
        ),

        # Show a plot of the generated distribution
        mainPanel(
           plotOutput("distPlot")
        )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {


    output$distPlot <- renderPlot({
        # generate bins based on input$bins from ui.R
        
        faithful |> tibble() |> ggplot(aes(x=waiting)) +
            geom_histogram(bins = input$bins) +
            theme_minimal(base_size = 16) +
            labs(x="Waiting time to next eruption (mins)",
                 title = "Histogram of Old Faithful Eruption Waiting Times")
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
